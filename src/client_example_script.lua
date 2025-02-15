--https://github.com/DEVIX7/Auto-vip-server-rejoiner
--client_example_script.lua
function callhost()
    local request = request or http.request or http_request
    local call = request({Url="http://127.0.0.1:8080/main",Method="POST",Body="connect-to-vip-server",Headers={["Content-Type"]="text/plain"}})
    if string.find(tostring(call.Body):lower(),"true") then
        game:GetService("Players").LocalPlayer:Kick("AVSRJ: Server ready. End of session player.");task.wait(1);game:Shutdown()
    end
end