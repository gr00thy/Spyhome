from colorama import init, Fore, Back, Style

#TITLE

init()
print(Fore.YELLOW+"")
print(Fore.YELLOW+"  ██████  ██▓███ ▓██   ██▓ ██░ ██  ▒█████   ███▄ ▄███▓▓█████ ")
print(Fore.YELLOW+"▒██    ▒ ▓██░  ██▒▒██  ██▒▓██░ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ ")
print(Fore.YELLOW+"░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░▒██▀▀██░▒██░  ██▒▓██    ▓██░▒███   ")
print(Fore.YELLOW+"  ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░░▓█ ░██ ▒██   ██░▒██    ▒██ ▒▓█  ▄ ")
print(Fore.YELLOW+"▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░░▓█▒░██▓░ ████▓▒░▒██▒   ░██▒░▒████▒")
print(Fore.YELLOW+"▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░")
print(Fore.YELLOW+"░ ░▒  ░ ░░▒ ░     ▓██ ░▒░  ▒ ░▒░ ░  ░ ▒ ▒░ ░  ░      ░ ░ ░  ░")
print(Fore.YELLOW+"░  ░  ░  ░░       ▒ ▒ ░░   ░  ░░ ░░ ░ ░ ▒  ░      ░      ░   ")
print(Fore.YELLOW+"      ░           ░ ░      ░  ░  ░    ░ ░         ░      ░  ░")
print(Fore.YELLOW+"                  ░ ░                                        ")
print("")
print(Fore.GREEN+"v1.0")
print("")

# MENU

while True:
    menu = int(input(Fore.GREEN+"""
    MENU
    (1)-- Opcion 1
    (2)-- Opcion 2 
    (3)-- Opcion 3  
    (4)-- Opcion 4
    (0)-- Salir                                                
    """))

    if menu == 1:
        print("Opcion 1")
    elif menu == 2:
        print("Opcion 2")
    elif menu == 3:
        print("Opcion 3")
    elif menu == 4:
        print("Opcion 4")
    else:
        break
