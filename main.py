import os
import requests as r
import schedule
import time
from twilio.rest import Client
      

def job():
    result = r.get(os.environ.get('doge_price_url'))
    price_doge = round(result.json()["data"]["market_data"]["price_usd"],5)
    if price_doge < 0.16:
        account_sid = os.environ.get('twilio_acc')
        auth_token = os.environ.get('twilio_token')
        client = Client(account_sid, auth_token)
        time_of_request = result.json()["status"]["timestamp"][:16]
        message = client.messages \
                        .create(
                            body="Hey bro, Doge coin price is at " + str(price_doge) + " at " + str(time_of_request) ,
                            from_=os.environ.get('twilio_phone'),
                            to=os.environ.get('twilio_dest_phone')
                        )
        print("Message Sent!")

schedule.every(1).hours.do(job)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)