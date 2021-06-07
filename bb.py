import requests
import json
from dhooks import Webhook, Embed
from threading import Thread
import time
import webbrowser
from playsound import playsound

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36' }

hook = Webhook("https://discord.com/api/webhooks/851272957195583488/9nNHwxzYGZglPWsIf8DmTsBNABnnYI_AK2bylacDS1eQ52DhwKbtkZtPnatswHh-lg9M")

sku = input("Enter Product SKU:")
request = requests.get(f"https://www.bestbuy.ca/ecomm-api/availability/products?accept=application%2Fvnd.bestbuy.standardproduct.v1%2Bjson&accept-language=en-CA&skus="+sku, headers=headers)
availability = json.loads(request.content)
stock = availability["availabilities"][0]["shipping"]["quantityRemaining"]

def checking():
    while True:
        if stock == 0:
            time.sleep(10)
            print("Out of Stock")
            
        else:
            
            embed = Embed(
    
    color=0x5CDBF0,
    timestamp='now'
    )
            embed.set_author(name='Product In Stock')
            embed.add_field(name='Stock: ', value=stock)
            embed.add_field(name='Link:',value="https://www.bestbuy.ca/en-ca/product/"+sku)


            print("In Stock")
            hook.send(embed=embed)
            playsound("mixkit-positive-interface-beep-221.wav")
            print(stock)
            time.sleep(30)
            





checking()