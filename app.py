from twilio.rest import Client

from dotenv import load_dotenv
import os


load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid,auth_token)



message = client.messages \
    .create (
        body="This is a Twilio messsage.",
        messaging_service_sid=os.environ.get('TWILIO_MSG_SID'),
        to='XXXXXXXXX'
    )

print(message.sid,"sent as a success!")