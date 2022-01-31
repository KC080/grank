from math import e
from requests import post, get
from utils.logger import register
from time import sleep
from json import loads

def buy(log, token, channel_id, timeout, logging, item, cwd, ID):
    request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": f"pls buy {item}"})
    
    if request.status_code != 200 :
        if logging["warning"]:
            register(log, "WARNING", f"Failed to send command `pls buy`. Status code: {request.status_code} (expected 200). Aborting command.")
        return
    
    if logging["debug"]:
        register(log, "DEBUG", "Successfully sent command `pls buy`.")
    
    latest_message = None
    
    for _ in range(0, timeout):
        sleep(1)
        
        request = get(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token})
        
        if request.status_code != 200:
            continue

        latest_message = loads(request.text)[0]
        
        if latest_message["author"]["id"] == "270904126974590976" and latest_message["referenced_message"]["author"]["id"] == ID:
            if logging["debug"]:
                register(log, "DEBUG", f"Got Dank Memer's response to command `pls buy {item}`.")
            break
        else:
            continue
       
    if latest_message is None or latest_message["author"]["id"] != "270904126974590976":
        if logging["warning"]:
            register(log, "WARNING", f"Timeout exceeded for response from Dank Memer ({timeout} second(s)). Aborting command.")
        return
        
    if latest_message["content"] == "Far out, you don't have enough money in your wallet or your bank to buy that much!!":
        from scripts.balance import balance
        bal = balance(log, token, channel_id, timeout, logging, ID)
        
        if bal[0]:
            bal = bal[-1]
            
            from json import load
    
            data = load(f"{cwd}/data.json")
            
            bank = int(latest_message["embeds"][0]["description"].split(":")[-1].split(" / ")[0].repalce("⏣", ""))
            wallet = int(latest_message["embeds"][0]["description"].split("\n")[0].split("⏣")[-1])
            
            if wallet - data["price"][item] > 0:
                request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": f"pls buy {item}"})
    
                if request.status_code != 200:
                    if logging["warning"]:
                        register(log, "WARNING", f"Failed to send command `pls buy {item}`. Status code: {request.status_code} (expected 200).")
                    return
                
                if logging["debug"]:
                    register(log, "DEBUG", f"Successfully sent command `pls buy {item}`.")
            elif (wallet + bank) - data["item"] > 0:
                amount = (wallet + bank) - data["item"]
                
                request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": f"pls with {amount}"})
    
                if request.status_code != 200:
                    if logging["warning"]:
                        register(log, "WARNING", f"Failed to send command `pls with {amount}`. Status code: {request.status_code} (expected 200).")
                    return
                
                if logging["debug"]:
                    register(log, "DEBUG", f"Successfully sent command `pls with {amount}`.")
                    
                request = post(f"https://discord.com/api/v8/channels/{channel_id}/messages", headers={"authorization": token}, data={"content": f"pls buy {item}"})
    
                if request.status_code != 200:
                    if logging["warning"]:
                        register(log, "WARNING", f"Failed to send command `pls buy {item}`. Status code: {request.status_code} (expected 200).")
                
                if logging["debug"]:
                    register(log, "DEBUG", f"Successfully sent command `pls buy {item}`.")
            elif logging["warning"]:
                register(log, "WARNING", f"Insufficient funds to buy a {item}")
                   
    elif latest_message["embeds"][0]["author"]["name"].lower() == f"successful {item} purchase":
        if logging["debug"]:
            register(log, "DEBUG", f"Successfully bought {item}.")