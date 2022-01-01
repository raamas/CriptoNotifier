import time
import requests

def getAssetPrice(asset_paircode):
    r = requests.get("https://api.coinbase.com/v2/prices/{}-COP/buy".format(asset_paircode))
    r = r.json()["data"]["amount"]
    return float(r)

def sendEmail(msg):
    import smtplib, ssl

    port = 465  # For SSL
    password = "password"

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("your notifier email@gmail.com", password)
        server.sendmail("your notifier email@gmail.com", "your@mail",msg)
    print(msg)

t = time.localtime()
current_time = int(time.strftime("%H", t))

# log = open("timelog.txt","a")
# lastTime = log.readlines()[-1]
# nextTime = lastTime + 5
# if nextTime >= 23:
#     nextTime = 5

assets = [
    {"name":"Cardano","paircode":"ADA", "price":0},
    {"name":"Kryll","paircode":"KRL", "price":0},
    {"name":"Orchid","paircode":"OXT", "price":0}
]

hours = [7,14,21,19]
while True:
    if current_time in hours:
        for asset in assets:
            asset["price"] = getAssetPrice(asset["paircode"])
            if asset["price"] < 1000 or asset["price"] > 3000:
                sendEmail("Subject: {} PRICE ALERT \n {} price is {}".format(asset["name"], asset["name"], asset["price"]))
        # if nextTime == int(current_time):
