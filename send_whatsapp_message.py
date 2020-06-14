from twilio.rest import Client
from send_message_and_return_sid import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


if __name__ == '__main__':
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='body',
        to='whatsapp:+12065791501',
    )

    print(message.sid)

