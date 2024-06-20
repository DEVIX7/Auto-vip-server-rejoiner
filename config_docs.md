# Docs | Config file

## Link Configuration

Configure details for rejoin into the VIP server:

### Link
- Specifies the link used to log into a VIP server.
- Default: `None`
```json
"link": "string"
```

### Message Link
- Using a link to the vip server from a client message.
- Default: `false`
```json
"msglink": "boolean"
```

Example client message (**link only!**):

```
https://www.roblox.com/games/0?privateServerLinkCode=0
```

### Android VIEW (aka method 2 to open the link)
- Opening a link using standard android actions.
- Default: `false`
```json
"androidVIEW": "boolean"
```

## WebSocket Configuration

Configure the WebSocket connection details:

### IP Address
- Specifies the IP address to which the client will connect.
- Default: `localhost`
```json
"ip": "string"
```

### Port
- Specifies the port separating the host from other applications.
- Default: `8126`
```json
"port": "number"
```

## Version Information

Displays the current version of the script. **DO NOT EDIT**

- Default: `current version`
```json
"version": "number"
```

# Made by DEVIX7
[Auto VIP Server Rejoiner](https://github.com/DEVIX7/Auto-vip-server-rejoiner)
