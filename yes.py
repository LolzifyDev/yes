####################
#    LolzOS 1.0    #
#  VSCode Edition  #
#                  #
#    Created By    #
#     Lolz.ify     #
####################

# For more credits
# Go to https://pastebin.com/DDW0mhH4
# Thank you,
# -Lolzify

from dataclasses import dataclass
import os
import time
import random
os.system('clear')
invalid_chars = ["", " ", "+", "=", "[", "]", "#",] # Add more soon
sys_ver = ["LXS1", "LXS2", "LXS3", "LXS-Core",] # Add more soon (?)
user_sys_ver = random.choice(sys_ver)
user = "test"
password = "test1234"
user_input = 0
"""
def askName():
    user = input("Nickname: ")
    if str(invalid_chars) in user:
        print("Error. Invalid characters.")
        askName()
"""
print("LolzOS VSCode Edition.")
print("Part of the LolzProject.\nThe LolzProject is maintained by Lolzify.")
time.sleep(6)
os.system('clear')
# askName()
data = None
locked = False
perms = "Admin"
os.system('clear')

print("'help' for commands")
while True:
    cmd = input(f"{user}>>> ")
    if cmd == "help":
        print("help : commands\nquit : close the os\nadv-help : more commands")
    elif cmd == "quit":
        print("Shutting down system...")
        time.sleep(3)
        quit()
    elif cmd == "adv-help":
        print("data [arg (~read , ~write , ~del)]\ninfo [arg (~system , ~user)]")
        print("lock [arg (NONE)]")
    elif cmd == "data":
        print("Missing arg: [~read , ~write , ~del]")
    # Data Scripts Start
    elif cmd == "data ~read":
        if data == None:
            print("No Data to Display.")
        else:
            print(data)
    elif cmd == "data ~write":
        print("WARNING: Writing new data will overwite old data.")
        data = input("data>>> ")
        if data == " " or "":
            print("Data contains invalid characters.")
            data = None
        else:
            print("Data has been stored.")
    elif cmd == "data ~del":
        print("Deleting data...")
        time.sleep(3)
        print("Data has been deleted.")
        data = None
    # Info Script Start
    elif cmd == "info":
        print("Missing arg: [~system , ~user]")
    elif cmd == "info ~system":
        print(f"System Build: LolzOS (VSCode Edition, Running with {user_sys_ver})")
        print("System Version: 1.B (1.0 Beta, Snapshot: -M.15.22)")
    elif cmd == "info ~user":
        print(f"User nickname: {user}\nPerms: {perms}")
    # Lock Script Start
    elif cmd == "lock":
        locked = True
        while locked == True:
            os.system('clear')
            user_input = input("Password: ")
            if user_input == password:
                print("Unlocked.")
                locked = False
                time.sleep(3)
                os.system('clear')
            else:
                print("Incorrect password!")
                time.sleep(3)
    elif cmd == "cmd":
        pass
