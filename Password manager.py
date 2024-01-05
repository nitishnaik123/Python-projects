W = input(" Welcome! You can save your passwords here.Press Enter to go ahead")
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, " ,Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to enter a new password or view existing ones (view,add), press q to quit ?")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
