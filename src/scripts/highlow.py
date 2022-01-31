from requests import post, get
from utils.logger import register
from time import sleep
from json import loads

def highlow(log, token, channel_id, timeout, logging, ID):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": "pls hl"})
    
    if request.status_code != 200:
        if logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls highlow`. Status code: {request.status_code} (expected 200). Aborting command.")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls highlow`.")
    
    latest_message = None
    
    for _ in range(0, timeout):
        sleep(1)
        
        request = get(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token})
        
        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] == "270904126974590976" and latest_message["referenced_message"]["author"]["id"] == ID:
            if logging["debug"]:
                register(log, "DEBUG", "Got Dank Memer's response to command `pls highlow`.")
            break
        else:
            continue
       
    if latest_message is None or latest_message["author"]["id"] != "270904126974590976":
        if logging["warning"]:
            register(log, "WARNING", f"Timeout exceeded for response from Dank Memer ({timeout} second(s)). Aborting command.")
        return
    
    number = int(latest_message["embeds"][0]["description"].split("**")[-2])
      
    data = {
        "application_id": 270904126974590976,
        "channel_id": channel_id,
        "type": 3,
        "data": {
            "component_type": 2,
            "custom_id": latest_message["components"][0]["components"][0]["custom_id"] if number > 50 else latest_message["components"][0]["components"][2]["custom_id"] if number < 50 else latest_message["components"][0]["components"][1]["custom_id"]
        },
        "guild_id": latest_message["message_reference"]["guild_id"],
        "message_flags": 0,
        "message_id": latest_message["id"]
    }
    
    request = post(f"https://discord.com/api/v9/interactions", headers={"authorization": token}, json=data)
    
    if request.status_code == 200 or request.status_code == 204:
        if logging["debug"]:
            register(log, "DEBUG", "Successfully interacted with button on Dank Memer's response to command `pls highlow`.")
    elif logging["warning"]:
        register(log, "WARNING", f"Failed to interact with button on Dank Memer's response to command `pls highlow`. Status code: {request.status_code} (expected 200 or 204).")