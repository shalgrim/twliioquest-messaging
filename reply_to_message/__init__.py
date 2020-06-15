"""Respond to Incoming SMS for TwilioQuest"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


NGROK_SUBDOMAIN = '953334ba1618'

app = Flask(__name__)


# Create a route to handle incoming SMS messages
# This is where the magic happens!
@app.route('/sms', methods=['GET', 'POST'])
def sms_ahoy_reply():
    print(
        f'Incoming message from {request.values.get("From")}: {request.values.get("Body")}'
    )

    # Here', we're generating TwiML using the Python helper library
    resp = MessagingResponse()
    # resp.message('TwilioQuest rules', action='/status_callback')
    resp.redirect('http://www.foo.com/nextInstructions')

    return str(resp)


@app.route('/status_callback', methods=['POST'])
def sms_ahoy_reply_status_callback():
    sid = request.values.get('MessageSid')
    status = request.values.get('MessageStatus')
    print(status, sid)
    return status + sid


@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    resp = MessagingResponse()
    resp.message("What's app, doc?", action='/status_callback')
    return str(resp)


if __name__ == '__main__':
    app.run(port=8767)
