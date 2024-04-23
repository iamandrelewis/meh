from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("""Good day, my name is from the unclaims department. 
        This is about your cheque for 18.5 millions dollars. If you were not contacted by one of agents about this, you can give me a call back at 2513599280. 
        Have a great day and god bless.""", voice='Polly.Amy')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
