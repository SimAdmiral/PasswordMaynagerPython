__author__ = "Sim Admiral"
import pickle
from getpass import getpass
import os
import clipboard
from signal import signal, SIGINT
from sys import exit

print("**************************************************************************")
print("Password saver. You can store here all your passwords and aditions informations")
print("This is Cmd Package")
print("Author: Sim Admiral")
print("Last update: 13.10.2021")
print("**************************************************************************")
print()
print()

dataHolder = []
alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
def loaddate():
    global dataHolder
    with open(filepath, 'rb') as file:
        while True:
            try:
                data = pickle.load(file)
                o=[]

                for index, r in enumerate(data):
                    p=[a for a in r]
                    for i, v in enumerate(p):
                        p[len(p) - i - 1:] = reversed(p[len(p) - i - 1:])
                    o.append("".join(p))

                dataHolder.append(o)
                # print(o[0] + " : ".rjust(30 - len(o[0])) + o[1].rjust(10 + len(o[1])))
            except:
                file.close()
                break
        file.close()
    

    s = {i[0]:i for i in dataHolder}
    dataHolder = [s[i] for i in sorted(s, key=str.lower)]
    del s

o=input("Do you want select file with passwords from actual directorie?: y\\n ")
if o.lower() == 'y':
    print("Select number of file with your saved passwords: ")
    print("-"*30)
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        for index, i in enumerate(filenames): print(f"| {index+1}: {i}")

    filenumber = int(input("Selected file number is: "))
    filepath = dirpath + "\\" + filenames[filenumber-1]
    filepath = filepath.replace('\\', '\\\\')

    #load Data
    loaddate()
elif o.lower()=='n':
    print("Create new file:")
    print()
    for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):pass

    filename = input("Create file name: ")
    filepath = dirpath + "\\" + filename
    filepath = filepath.replace('\\', '\\\\')

    if input("Do you want create file password? Y\\n ").lower() == 'y':
        newPassword = getpass("Write file passsord: ")
        if getpass("Confirm file passsord: ") == newPassword:
            print("Success")
else:
	exit(0)
print(filepath)

#METHODS

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    savedata()
    exit(0)
def clip(data):
    global dataHolder

    if data[1].lower()=='p':
        clipboard.copy(dataHolder[int(data[0])-1][1])
    elif data[1].lower()=='e':
        clipboard.copy(dataHolder[int(data[0])-1][2])
    elif data[1].lower()=='l':
        clipboard.copy(dataHolder[int(data[0])-1][5])
    elif data[1].lower()=='u':
        clipboard.copy(dataHolder[int(data[0])-1][4])
    elif data[1].lower()=='t':
        clipboard.copy(dataHolder[int(data[0])-1][0])
    elif data[1].lower()=='d':
        clipboard.copy(dataHolder[int(data[0])-1][6])
    elif data[1].lower()=='n':
        clipboard.copy(dataHolder[int(data[0])-1][3])
    else:
        print("Wrong command")

def savedata():
    global dataHolder
    with open(filepath, 'wb') as file:
        if len(dataHolder)!=0:
            for data in dataHolder:
                passType = str(data[0])
                password = str(data[1])
                email = str(data[2])
                name = str(data[3])
                username = str(data[4])
                lastname = str(data[5])
                description = str(data[6])
                password = [i for i in password]
                passType1 = [i for i in passType]

                for i, v in enumerate(password):
                    password[i:] = reversed(password[i:])
                password = "".join(password)
                for i, v in enumerate(passType1):
                    passType1[i:] = reversed(passType1[i:])
                passType1 = "".join(passType1)

                if email != '-':
                    email = [i for i in email]
                    for i, v in enumerate(email):
                        email[i:] = reversed(email[i:])
                    email = "".join(email)
                if name != "-":
                    name = [i for i in name]
                    for i, v in enumerate(name):
                        name[i:] = reversed(name[i:])
                    name = "".join(name)
                if username != "-":
                    username = [i for i in username]
                    for i, v in enumerate(username):
                        username[i:] = reversed(username[i:])
                    username = "".join(username)
                if lastname != "-":
                    lastname = [i for i in lastname]
                    for i, v in enumerate(lastname):
                        lastname[i:] = reversed(lastname[i:])
                    lastname = "".join(lastname)
                if description != "-":
                    description = [i for i in description]
                    for i, v in enumerate(description):
                        description[i:] = reversed(description[i:])
                    description = "".join(description)

                pickle.dump([passType1, password, email, name, username, lastname, description], file, protocol=4)
        file.close()

def showtypes():
    global dataHolder
    for i in dataHolder:
        print(i[0])
def showall():
    global dataHolder
    a1 = max([len(i[0]) for i in dataHolder])+2
    a2 = max([len(i[1]) for i in dataHolder])+2
    a3 = max([len(i[2]) for i in dataHolder])+2
    a4 = max([len(i[3]) for i in dataHolder])+2
    a5 = max([len(i[4]) for i in dataHolder])+2
    a6 = max([len(i[5]) for i in dataHolder])+2
    a7 = max([len(i[6]) for i in dataHolder])

    print(f"".ljust(len(str(len(dataHolder)) + '#')), end=" ")
    print("Type".ljust(a1), "Password".ljust(a2), "Email".ljust(a3), "Name".ljust(a4), "Username".ljust(a5), "Lastname".ljust(a6), "Description".ljust(a7))
    for index,i in enumerate(dataHolder):
        print(f"{index+1}#".ljust(len(str(len(dataHolder))+'#')), end=" ")
        print(i[0].ljust(a1), i[1].ljust(a2), i[2].ljust(a3), i[3].ljust(a4), i[4].ljust(a5), i[5].ljust(a6), i[6].ljust(a7) , end=" ")
        print()
def deleteall():
    global dataHolder
    dataHolder = []
def addpassword(data):
    global dataHolder
    if data[0][0]=='-':
        holder=["-" for i in range(7)]

        for index, i in enumerate(data[::2]):
            print(i)
            if i=='-t':
                holder[0]=data[((index+1)*2)-1]
            if i=='-p':
                holder[1] = data[((index + 1) * 2) - 1]
            if i=='-d':
                holder[6] = data[((index + 1) * 2) - 1]
            if i=='-e':
                holder[2] = data[((index + 1) * 2) - 1]
            if i=='-n':
                holder[3] = data[((index + 1) * 2) - 1]
            if i=='-u':
                holder[4] = data[((index + 1) * 2) - 1]
            if i=='-l':
                holder[5] = data[((index + 1) * 2) - 1]
        print(holder)
        data=holder
    else:
        data1 = ['-' for i in range(7)]
        for index, i in enumerate(data):
            data1[index]=i
        data=data1

    for i in dataHolder:
        if i[0]==data[0]:
            if input("Actual data are in saved do you want overrite it? Y/n ").lower()=='y':
                dataHolder.remove(i)
                dataHolder.append(data)
            break
    else:
        dataHolder.append(data)


    s = {i[0].lower():i for i in dataHolder}
    dataHolder = [s[i] for i in sorted(s)]
    del s
def deletepassword(passType):
    global dataHolder
    for i in dataHolder:
        if i[0]==passType:
            dataHolder.remove(i)
def showpassword(dataType):
    global dataHolder

    for i in dataHolder:
        if i[0]==dataType:
            print(i)

    pass
def changepassword():
    global dataHolder
    if input("Do you wont to change your password? y/n ").lower()=='y':
        checkPass=getpass("Take a new password: ")
        inPass=getpass("Confirm your new password: ")
        if inPass==checkPass:
            addpassword("FilePassword", inPass, check=False)


signal(SIGINT, handler)

while True:

    inp = [''] + input("-> ").split()
    fix = False

    if len(inp)==1:
        print("give me some input")
        continue

    if len(inp)==2:
        if inp[1].lower() in ['e','q', 'exit', 'quit','exit()', 'quit()']:
            savedata()
            exit(0)
        elif inp[1].lower() in ["help", "/?"]:
            # SUPPORTED COMMANDS
            print()
            print("all supported commands are:")
            print()
            print("add password [type][password][email][name][username][lastname][description]")
            print("        -t      type")
            print("        -n      name")
            print("        -p      password")
            print("        -u      username")
            print("        -l      lastname")
            print("        -e      email")
            print("        -d      description")
            print()
            print("delete password [type] will delete password")
            print()
            print("delete all      will delete everythning")
            print("show types      will show you only types")
            print("show all        will show you everything")
            print("show password   [type] will show you serten type")
            print("clip [number] [letter]     you will copy the serten collum and row")
            print("                           by adding a collum which is number [12] ")
            print("                           and adding row which is [letter] from (t n p u l e d) ")
            print("                           you can see it on the top")
            print("                example | clip 2 p | will copy password from secend row")
            print("clear|cls       clear screen")
            print("help /?")
            print()
        elif inp[1].lower() in ["cls", "clear"]:
            os. system('cls')
        elif inp[1].lower() == "save":
            savedata()
            # loaddate()
        else:
            print("Invalid or unsupported command")

    if len(inp) ==3:
        type = "".join(inp[1:3]).lower()

        if type=="showall":
            showall()
        elif type=="showtypes":
            showtypes()
        elif type=="deleteall":
            deleteall()
        else:
            print("Invalid or unsupported command")

    if len(inp) > 3:
        type = "".join(inp[1:3]).lower()

        if type == "addpassword":
            if len(inp) >= 5:
                print(inp[3:])
                addpassword(inp[3:])
            else: print("Invalid or unsupported command")
        elif inp[1].lower()=="clip":
            clip([inp[2], inp[3]])
        elif type == "changestuff":
            if len(inp) >=5:
                changepassword(inp[3:])
            else: print("Invalid or unsupported command")
        elif type=="deletetype":
            if len(inp)==4:
                deletepassword(inp[3])
            else: print("Invalid or unsupported command")
        elif type=="showtype":
            if len(inp)==4:
                showpassword(inp[3])
            else: print("Invalid or unsupported command")
        else:
            print("Invalid or unsupported command")
