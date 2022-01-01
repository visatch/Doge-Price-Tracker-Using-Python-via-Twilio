import os
import requests as r
import schedule
import time
from twilio.rest import Client


def priceChecker():
    result = r.get(os.environ.get('doge_price_url'))
    price_doge = result.json()["data"]["market_data"]["price_usd"]
    time_of_request = result.json()["status"]["timestamp"][:16]
    if price_doge >= 18:
        job()

def job(price_doge):
    account_sid = os.environ.get('twilio_acc')
    auth_token = os.environ.get('twilio_token')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Hey bro, Doge coin price is at " + price_doge + " ",
                        from_=os.environ.get('twilio_phone'),
                        to=os.environ.get('twilio_dest_phone')
                    )

    print("Message Sent!")

schedule.every().minute.at(":00").do(priceChecker)

if __name__ == "__main__":
    schedule.run_pending()
    time.sleep(1)