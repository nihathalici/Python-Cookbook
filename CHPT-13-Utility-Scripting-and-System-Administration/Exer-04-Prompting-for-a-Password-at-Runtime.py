# Exer-04-Prompting-for-a-Password-at-Runtime

import getpass

user = getpass.getuser()
passwd = getpass.getpass()

if svc_login(user, passwd):
    print("Yay!")
else:
    print("Boo!")

###

user = input("Enter your username: ")
