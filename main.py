def login():
    print("a simple ting!")
    print("--------------------------------------------")
    print("\t\tlogin")
    print("--------------------------------------------\n")
    input("username: ")
    input("password: ")



def main():
    print("a simple ting!")
    print("--------------------------------------------\n")
    print("1. Add/Update leads.......................[ ]")
    print("2. Make calls.............................[ ]\n")
    print("3. Settings...............................[ ]\n")
    print("============================================")
    input('Select an option: ')

def leads_menu():
    print("Add/Update leads")
    print("--------------------------------------------\n")
    print("1. Search................................[ ]")
    print("2. Upload leads..........................[ ]\n")
    print("0. Go back............................[ <- ]")
    print("============================================")
    input('Select an option: ')

def settings_menu():
    print("Settings")
    print("--------------------------------------------\n")
    print("TWILIO ACCOUNT SID",end=" ")
    print("INACTIVE")
    print("TWILIO AUTH TOKEN", end=" ")
    print("INACTIVE")
    print("CALL PROMPT", end=" ")
    print("INACTIVE")
    