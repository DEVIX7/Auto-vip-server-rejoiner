# Auto VIP Server Rejoiner

**Version 1.5**  
*Android Termux*

### Update Log:
- **Version 1.5**  
  - Code refactor  
  - ~~WebSocket~~  
  - ~~open-url~~  

- **Repository Update**  
  - Improved structure

## Requirements

The client script requires the **Request** library to function properly.

## Installation (Android)

1. **Install Termux**  
   Download and install [Termux](https://f-droid.org/en/packages/com.termux/) from the official source (available for devices and emulators).

2. **Update and Install Dependencies**  
   Open Termux and execute the following commands:
   ```bash
   pkg update
   pkg upgrade
   pkg install wget
   pkg install python
   ```

3. **Download Code and Configuration Files**  
   Fetch the necessary files using the following commands:
   ```bash
   wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/refs/heads/main/src/config.json
   wget https://raw.githubusercontent.com/DEVIX7/Auto-vip-server-rejoiner/refs/heads/main/src/main_android_termux.py
   ```

4. **Edit Configuration File**  
   Modify the `config.json` file with your preferred private server link:
   ```bash
   nano config.json
   ```
   Example:
   ```json
   {
       "link": "https://www.roblox.com/games/0?privateServerLinkCode=0"
   }
   ```
   - Save the changes by pressing `Ctrl+S`, then exit with `Ctrl+X`.

5. **Run the Script**  
   Start the script with:
   ```bash
   python main_android_termux.py
   ```
> [!NOTE]
> If an error occurs during the initial launch after installing the dependencies, simply restart the script.
---
### Made by DEVIX7  
> [!IMPORTANT]
> ## [SHA-256 Checksum Verification](https://github.com/DEVIX7/Auto-vip-server-rejoiner/tree/main/resources/checksums.sha256)