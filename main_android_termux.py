import re
import asyncio
import subprocess
import time
import json
#made by devix7
def colored_text(text, color):
    colors = {
        'reset': '\033[0m',
        'info': '\033[94m',
        'warn': '\033[93m',
        'success': '\033[92m',
        'bright_cyan': '\033[96m'
    }
    return f"{colors[color]}{text}{colors['reset']}"

with open('./config.json', 'r') as config_file:
    config = json.load(config_file)
    ip = config.get('ip', 'localhost')
    port = config.get('port', 8126)
    msglink = config.get('msglink', 'false') == 'true'
    androidVIEW = config.get('androidVIEW', 'false') == 'true'
    link = config.get('link', 'URL VIP SERVER HERE')

link_display = 'none' if link == 'URL VIP SERVER HERE' else link

try:
    import websockets
except ImportError:
    print(colored_text("Module 'websockets' not found. Auto-installing...", 'warn'))
    subprocess.run(['pip', 'install', 'websockets'], check=True)

def kill_roblox():
    pid_result = subprocess.run(['pgrep', '-o', '-f', 'com.roblox.client'], stdout=subprocess.PIPE, text=True)
    pid = pid_result.stdout.strip()

    print(colored_text("Closing application roblox...", 'warn'))

    if pid:
        subprocess.run(['kill', pid])

    time.sleep(5)

async def handle_client(websocket, path):
    try:
        async for message in websocket:
            print(f"Received message from client: {message}")
            
            if msglink:
                kill_roblox()
                print(colored_text("Opening link...", 'info'))
                open_url(message)

            if message == 'connect-to-vip-server':
                kill_roblox()
                print(colored_text("Opening link...", 'info'))
                open_url(link)

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")
    except Exception as e:
        print(f"Error: {e}")

def extract_place_id_and_code(url):
    match = re.search(r'/games/(\d+)\?privateServerLinkCode=(\d+)', url)
    if match:
        return match.groups()
    else:
        raise ValueError("Invalid URL format")

def open_url(url):
    if androidVIEW:
        place_id, private_server_code = extract_place_id_and_code(url)
        print(colored_text(f"Opening with android.view: roblox://placeID={place_id}&LinkCode={private_server_code}", 'info'))
        subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', f"roblox://placeID={place_id}&LinkCode={private_server_code}"], check=True)
    else:
        print(colored_text(f"Opening with termux: {url}", 'info'))
        subprocess.run(['termux-open-url', url], check=True)

if __name__ == "__main__":
    subprocess.run(['clear'], check=True)
    print(colored_text('''
   ___  _____   _______  ______
  / _ \/ __/ | / /  _/ |/_/_  /
 / // / _/ | |/ // /_>  <  / / 
/____/___/ |___/___/_/|_| /_/ 
     github.com/DEVIX7
    ''', 'bright_cyan'))

    print(colored_text("Auto vip server rejoiner \" version 1.4.2 (android termux)\n", 'info'))
    print(f"Config:\nmsglink: {msglink}\nlink: {link_display}\nip: {ip}\nport: {port}\nandroidVIEW: {androidVIEW}\n")

    server = websockets.serve(handle_client, ip, port)

    print(colored_text(f"WebSocket server started. Listening on ws://{ip}:{port}", 'success'))

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
