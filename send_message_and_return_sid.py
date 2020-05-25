import os

from twilio.jwt.access_token import AccessToken
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_API_KEY = os.getenv('TWILIO_API_KEY')
TWILIO_API_SECRET = os.getenv('TWILIO_API_SECRET')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')


if __name__ == '__main__':
    # token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET)
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_='+18588798141', body='this is a test', to='+12065791501'
    )
    print(message.sid)
