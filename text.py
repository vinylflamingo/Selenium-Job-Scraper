from twilio.rest import Client

def sendSms(hit):
    client = Client("ACCOUNT ID Removed For GitHub", "AUTH TOKEN RemovedFor Github")
    client.messages.create(to="YOUR PHONE NUMBER HERE",
                           from_="TWILIO PHONE NUMBER HERE",
                           body=f"Matches found: {hit}")
