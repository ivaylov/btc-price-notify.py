import requests
import json
import os
import time
import beepy as beep

while True:
    
    request = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true").text
    request = json.loads(request)
    price = request["bitcoin"]["usd"]
    change = request["bitcoin"]["usd_24h_change"]
    print("bitcoin price is:", '{:.2f}'.format(price), "24h change: %", '{:.2f}'.format(change))
    if change > 10:
        beep.beep('coin')  
        os.system(f"notify-send -t 10000 \" bitcoin price is %10 up:{'{:.2f}'.format(price)}\"")
    if change < -10:
        beep.beep('coin')  
        os.system(f"notify-send -t 10000 \" bitcoin price is %10 down:{'{:.2f}'.format(price)}\"")
    time.sleep(10)
