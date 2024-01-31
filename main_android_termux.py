import asyncio
import subprocess
import time
import json

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
    msglink = config.get('msglink', 'false')

try:
    import websockets
except ImportError:
    print(colored_text("Module 'websockets' not found. Auto-installing...", 'warn'))
    subprocess.run(['pip', 'install', 'websockets'])

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
            
            if config.get('msglink') == 'true':

                kill_roblox()

                print(colored_text("Opening link...", 'info'))
                subprocess.run(['termux-open-url', message])

            if message == 'connect-to-vip-server':

                kill_roblox()

                link = config.get('link', '')

                print(colored_text("Opening link...", 'info'))
                subprocess.run(['termux-open-url', link])

    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    subprocess.run(['clear'])
    print(colored_text('''
   ___  _____   _______  ______
  / _ \/ __/ | / /  _/ |/_/_  /
 / // / _/ | |/ // /_>  <  / / 
/____/___/ |___/___/_/|_| /_/ 
     github.com/DEVIX7
    ''', 'bright_cyan'))

    print(colored_text("Auto vip server rejoiner \" version 1.3.3 (android termux)\n", 'info'))

    server = websockets.serve(handle_client, ip, port)

    print(colored_text(f"WebSocket server started. Listening on ws://{ip}:{port}", 'success'))

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()

