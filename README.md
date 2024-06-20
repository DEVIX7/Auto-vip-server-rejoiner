# Auto VIP Server Rejoiner

Version 1.3.3
- Android Termux

### Update Log:
- Version 1.3.3
    - Added in config file:
        - Custom IP and Port
        - MSGLink - link to the VIP server sent by the client script
- Repo update
    - Added [docs for config file](https://github.com/DEVIX7/Auto-vip-server-rejoiner/blob/main/config_docs.md)

## Requirements

- The executor requires the WebSocket library.

## [Docs | Config file](https://github.com/DEVIX7/Auto-vip-server-rejoiner/blob/main/config_docs.md)

## Installation (Android)

1. Download and install [Termux](https://f-droid.org/en/packages/com.termux/) on your device/emulator.

2. Open Termux and enter the following commands:
```
pkg update
pkg upgrade
pkg install wget
pkg install python
```
3. Download code and config files:
```
wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/main/config.json
wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/main/main_android_termux.py
```
or (for step 1, 2 and 3)
```
pkg update && upgrade && pkg install wget && pkg install python && wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/main/config.json && wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/main/main_android_termux.py && nano config.json && python main_android_termux.py
```
4. Edit the config file:
```
nano config.json
```
Edit the "link" parameter. For example:
```json
{
    "link": "https://www.roblox.com/games/0?privateServerLinkCode=0",
    "version": "1.2"
}
```
Press Ctrl+X (^X), press "Y", and then press Enter.

5. Start the script:
```
python main_android_termux.py
```
# Made by DEVIX7
## [Checksums MD5](https://github.com/DEVIX7/Auto-vip-server-rejoiner/blob/main/checksums.md5)
