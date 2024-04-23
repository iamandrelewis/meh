import gspread
import twilio
import asyncio
from google.oauth2.service_account import Credentials
import make_calls
import os 
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1qePVgNk3WclaoYTOhx165_ZsqXKnGnFeb9QpG8GaH7Y"
workbook = client.open_by_key(sheet_id)

sheet = workbook.worksheet("Sep23 HERCULES Edition Octane")

leads = sheet.get_all_records()
async def run_leads():
    for i in leads:
        os.system('cls')
        print('----------------------------------------------------------------------------------\nMaking calls.....\n----------------------------------------------------------------------------------')
        await asyncio.sleep(1)
        print(f"\n{i['fname']} {i['lname']}\t\t\t\t\t\t     -> +1{i['phone']}")
        print('==================================================================================')
        print(f"[\t\t\t\t  {str(leads.index(i)+1)} out of {str(len(leads))} \t\t\t\t]")
        await asyncio.sleep(3)

        if  i['Called Status'] == 'FALSE':
            try:
                call = make_calls.make_call("+1" + str(i['phone']))
                print(call)
                sheet.update_acell(f'L{leads.index(i)+2}','True')
            except twilio.base.exceptions.TwilioRestException:
                print("Call failed")
                await asyncio.sleep(2)
                continue
            print('Call successful')
asyncio.run(run_leads())