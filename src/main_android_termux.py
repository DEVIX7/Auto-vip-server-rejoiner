#https://github.com/DEVIX7/Auto-vip-server-rejoiner
#main_android_termux.py
import subprocess 
import time
import json
import re
import threading
current_version = "1.5"
try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Module 'Flask' not found. Auto-installing...")
    subprocess.run(['pip', 'install', 'Flask'], check=True)
    from flask import Flask, request, jsonify
try:
    import requests
except ImportError:
    print("Module 'requests' not found. Auto-installing...")
    subprocess.run(['pip', 'install', 'requests'], check=True)
    import requests
time.sleep(1)
def check_version():
    try:
        response = requests.get("https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/refs/heads/main/resources/version.txt")
        response.raise_for_status()
        latest_version = response.text.strip()
        if latest_version != current_version:
            print(f"\nVersion differs: repo {latest_version}, current {current_version}. (If it works, ignore this.)\n")
    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")
subprocess.run(['clear']) 
print(r'''
   ___  _____   _______  ______
  / _ \/ __/ | / /  _/ |/_/_  /
 / // / _/ | |/ // /_>  <  / / 
/____/___/ |___/___/_/|_| /_/  
      github.com/DEVIX7
''')
print(f"Auto vip server rejoiner » version {current_version} (Android Termux)\n")
app = Flask("AVSRJ-SERVER")
with open("./config.json","r") as config_file:
    config = json.load(config_file)
    conf_ip = config.get('ip', '127.0.0.1')
    conf_port = config.get('port', 8080)
    conf_link = config.get('link', 'URL VIP SERVER HERE (IF YOU SEE THIS EDIT THE CONFIG!)')
print(f"CONFIG:\nIP: {conf_ip}:{conf_port}\nLINK: {conf_link}\n")
def kill_rblx():
    pid_result = subprocess.run(['pgrep', '-o', '-f', 'com.roblox.client'], stdout=subprocess.PIPE, text=True)
    pid = pid_result.stdout.strip()
    if pid:
        print("Process found, force kill")
        subprocess.run(['kill', '-9', pid])
    else:
        print("Not process found, btw (。_。)")
        print("Trying to restart...")
        subprocess.run(['am', 'start', '-S', '-n', 'com.roblox.client/com.roblox.client.startup.ActivitySplash'], stdout=subprocess.PIPE, text=True)
    time.sleep(5)
def extract_placeid_and_pscode(url):
    match = re.search(r'/games/(\d+)\?privateServerLinkCode=(\d+)', url)
    if match:
        return match.groups()
    else:
        raise ValueError("Invalid URL format")
def open_url(url):
    place_id, link_code = extract_placeid_and_pscode(url)
    print(f"Opening rblx:\nPlace ID: {place_id} | Link Code: {link_code}")
    subprocess.run(['am', 'start', '-a', 'android.intent.action.VIEW', '-d', f"roblox://placeID={place_id}&LinkCode={link_code}"], check=True)
def actions():
    time.sleep(5)
    kill_rblx()
    time.sleep(2)
    open_url(conf_link)
@app.route('/main', methods=['POST'])
def connect_to_vip_server():
    data = request.data.decode('utf-8').strip()
    if data == "connect-to-vip-server":
        response = jsonify(True)
        response.status_code = 200
        threading.Thread(target=actions).start()
        return response
    else:
        return jsonify(False)
if __name__ == '__main__':
    threading.Thread(target=check_version).start()
    app.run(host=conf_ip, port=conf_port)