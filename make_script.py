from twilio.twiml.voice_response import VoiceResponse
def generate_xml(script = None):
    response = VoiceResponse()
    if script is None:
        response.say("""Good day, my name is Chad Smith from the unclaims department. 
        This is about your cheque for 18.5 millions dollars. If you were not contacted by one of agents about this, you can give me a call back at 2513599280. 
        Have a great day and god bless.""")
    else:
        response.say(script)
    return response



