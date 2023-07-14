import colorama
from colorama import Fore

print(Fore.RED + "Starting.......\n")
print(Fore.BLUE + "           ------------------- ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |                  ")
print(Fore.BLUE + "           |       -----------")
print(Fore.BLUE + "           |       |         |")
print(Fore.BLUE + "           |       |         |   ------- |------| |       -------- |       | |      |-------| _________ |------| |-----|")
print(Fore.BLUE + "           |                 |   |       |      | |       |        |       | |      |       |     |     |      | |_____|")
print(Fore.BLUE + "           |                 |   |       |------| |       |        |       | |      |-------|     |     |      | |\_")
print(Fore.BLUE + "           -------------------   |------ |      | |------ |------- |-------| |----- |       |     |     |------| |  \_")
print(Fore.GREEN + " Plan ====== Free(Classic)")
print("------------------------------------------------------------------------------------------------\n\n")

o = 0
nc = 1
while (o == 0):
    op = int(input(Fore.YELLOW + "Enter your choice:\n2.multiplication\n3.division\n4.addition\n5.subtaction\n----------------> "))
    print("\n\n")
    if (op == 2):
        print("                                                   Session --",nc,"                                  ")
        no = float(input("Enter the number: "))
        p = float(input("Enter the other number: "))
        ans = no*p
        nc = nc + 1
        print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
    elif (op == 3):
        print("                                                   Session --",nc,"                                  ")
        no = float(input("Enter the divident: "))
        p = float(input("Enter the divisor: "))
        ans = no/p
        nc = nc + 1
        print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
    elif (op == 4):
        print("                                                   Session --",nc,"                                  ")
        no = float(input("Enter the number: "))
        p = float(input("Enter the other number: "))
        ans = no + p
        nc = nc + 1
        print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
    elif (op == 5):
        print("                                                   Session --",nc,"                                  ")
        no = float(input("Enter the number from which you want to substract: "))
        p = float(input("Enter the number which you want to subtract: "))
        ans = no - p 
        nc = nc + 1
        print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
    else:
        print("Thank you for using G-Calculator")