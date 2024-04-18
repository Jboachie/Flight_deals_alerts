from twilio.rest import Client
ACCOUNT_SID = "AC319e277bdc1c05c91b1acb75899dcaab"
ACCOUNT_TOKEN = "ef1e06c0bb737494cbef9f2531512672"
TWILIO_NO = "+447883319285"
PHONE_NUMBER = "+447930413653"

class NotificationManager:
    def __init__(self, text):
        client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)

        message = client.messages.create(
            to=PHONE_NUMBER,
            from_= TWILIO_NO,
            body= text
        )

        print(message.sid)