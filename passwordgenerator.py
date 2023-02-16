import random
import string
import os


#generatepassword
def generatepassword(symbols, length):
    password = ""
    characterlist = ""
    if symbols:
        characterlist = random.choices(string.ascii_letters + string.digits + string.punctuation , k=length)
    else:
        characterlist = random.choices(string.ascii_letters, k=length)

    for x in characterlist:
        password = password + x

    return password

def start():
    os.system("cls")
    print("Password generator v.1.0")
    print("------------------------")
    try:
        length = int(input("How many characters do you want to use? -> "))
        if length == 0:
            print("ERROR: You need to provide a value")
            return
    except:
        print("ERROR: Please enter an integer")
        return

    usesymbols = str(input("Do you want to include symbols? (yes/no) -> "))

    if usesymbols == "yes":
        symbols = True
    elif usesymbols == "":
        print("ERROR: You need to provide a value")
        return
    else:
        symbols = False

    print("Your password: " + str(generatepassword(symbols, length)))

start()
repeat = 1
while repeat == 1:
    runagain = str(input("Do you want to run password generator again? (yes/no) -> "))
    if runagain == "yes":
        start()
    else:
        repeat = 0