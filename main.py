import os
from twilio.rest import Client

account_sid = os.environ.get('twilio_acc')
auth_token = os.environ.get('twilio_token')
print(account_sid)
print(auth_token)

# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Hey bro how are you doing",
#                      from_=os.environ.get('twilio_phone'),
#                      to=os.environ.get('twilio_dest_phone')
#                  )

# print(message.sid)

if __name__ == "__main__":
    print("hello")