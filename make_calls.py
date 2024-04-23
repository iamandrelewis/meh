import os
from twilio.rest import Client

account_sid = "ACce52691e30960fc5a2693f257ccb4ede"
auth_token = "0fbf410b81771971b4b66d9bf3bf1107"
client = Client(account_sid, auth_token)

def make_call(to_number:str) -> Client.calls:
  call = client.calls.create(
    twiml="""<Response><Say>Good day, my name is Chad Smith from the unclaims department. 
        This is about your cheque for 18.5 millions dollars. If you were not contacted by one of agents about this, you can give me a call back at 2 5 1 3 5 9 9 2 8 0.
        That's 2 5 1 3 5 9 9 2 8 0. 
        Have a great day and god bless.</Say></Response>""",
    to=to_number,
    from_="+12513599280"
  )
  print(call.sid)
  #return call

make_call("+18764608874")
