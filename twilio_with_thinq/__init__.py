from twilio.rest import TwilioRestClient
import sys

class TwilioWrapper:
	TWIML_RESOURCE_URL = "http://cris.viralearnings.com/twiml/get_response"

	def __init__(self, customer_number, twilio_account_sid, twilio_account_token, twilio_phone_number):
		self.customer_number = customer_number
		self.twilio_account_sid = twilio_account_sid
		self.twilio_account_token = twilio_account_token
		self.twilio_phone_number = twilio_phone_number
		self.client = TwilioRestClient(twilio_account_sid, twilio_account_token)

	def isClientValid(self):
		return (not self.client is None)

	def call(self):
		if not self.isClientValid():
			return "Invalid Twilio Account details."
		try:
			call = self.client.calls.create(url=TwilioWrapper.TWIML_RESOURCE_URL,
				to=self.customer_number,
				from_=self.twilio_phone_number)
			return call.sid
		except:
			return sys.exc_info()[0]

	# def test_call(self):
	# 	client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
	# 		to=self.customer_number,
	# 		from_=self.twilio_phone_number)

