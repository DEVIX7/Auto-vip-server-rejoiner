function callhost()
    local socket = WebSocket.connect("ws://localhost:8126")
    socket:Send("connect-to-vip-server")
end