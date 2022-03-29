import requests
import json
import os
import time
import beepy as beep

while True:
    
    request = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&ids=bitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h").text
    request = json.loads(request)
    
    price = request[0]["current_price"]
    change = request[0]["price_change_percentage_1h_in_currency"]
    market_cap = request[0]["market_cap"]
    print("Bitcoin price is:", '{:.2f}'.format(price), "1h change: %", '{:.2f}'.format(change), "Market Cap:", '{:.2f}'.format(market_cap))
    if change > 1:
        beep.beep('coin')  
        os.system(f"notify-send -t 10000 \" bitcoin price is %1 up:{'{:.2f}'.format(price)}\"")
        print("Bitcoin price is:", '{:.2f}'.format(price), "1h change: %", '{:.2f}'.format(change), "Market Cap:", '{:.2f}'.format(market_cap))
    time.sleep(10)
