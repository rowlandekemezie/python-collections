
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC26af82b0fd334974daa4bb3e3a642131"
auth_token = "a41d2775c362ac9946d70d18b4a169e0"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+2348067721742", 
	messaging_service_sid="MG20955e562c80e39b13b4cdaee6cf2d4f",
      body="Rowland. We are reaching you from twilio!")