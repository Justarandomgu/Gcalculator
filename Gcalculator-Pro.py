import colorama
from colorama import Fore
import json

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
pas = input("\n" + Fore.CYAN + "Please enter the password: ")
user = open ('Userdata.json','r')
data = user.read()
obj = json.loads(data)
#data var
name = str(obj['name'])
plan = str(obj['plan'])
password = str(obj['password'])
if (pas == password):
    print("Welcome,", name)
    print(Fore.GREEN + " Plan ======",plan)
    print("------------------------------------------------------------------------------------------------\n\n")

    o = 0
    nc = 0
    while (o == 0):
        op = int(input(Fore.YELLOW + "Enter your choice:\n1.power calculation                               11.Unit convertor (meter)                               21.Finder(Sin, Cos, Tan)\n2.multiplication                                  12.Unit convertor (litre)                               22.Time partitioner and difference finder\n3.division                                        13.Unit Converter (gram)\n4.addition                                        14.Area finder(2D)\n5.subtaction                                      15.volume finder(3D)\n6.division (remainder)                            16.Temperature convertor\n7.root finder"
                                     "                                     17.Factor Finder\n8.division (divident)                             18.Prime Factoriser\n9.division (divisor)                              19.Multiple Finder\n10.division (divisor with remainder)              20.Multiple within range\n----------------> "))
        print("\n\n")
        if (op == 1):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            p = int(input("Enter the power: "))
            ans = no**p
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 2):
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
        elif (op == 6):
            print("                                                   Session --",nc,"                                  ")
            no = int(input("Enter the divident: "))
            p = int(input("Enter the divisor: "))
            ans = no%p 
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 7):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the number: "))
            import math
            ans = math.sqrt(no)
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 8):
            print("                                                   Session --",nc,"                                  ")        
            opt = int(input("Do you have you remainder as 0? (1.No ; 2.Yes): "))
            if (opt == 1):
                no = float(input("Enter the divisor: "))
                p = float(input("Enter the quotient: "))
                ans = no*p 
                nc = nc + 1
                print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
            else:
                no = float(input("Enter the divisor: "))
                p = int(input("Enter the quotient: "))
                re = int(input("Enter the remainder: "))
                ans = (no*p) + re
                nc = nc + 1
                print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 9):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the quotient: "))
            p = float(input("Enter the divident: "))
            ans = p/no
            nc = nc + 1
            print("The answer is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 10):
            print("                                                   Session --",nc,"                                  ")
            no = float(input("Enter the quotient: "))
            p = float(input("Enter the divident: "))
            ans = p/no
            nc = nc + 1
            rem = p%no
            print("The remainder is",rem)
            print("The divisor (in interger) is",int(ans))
            print("The divisor (in decimal) is",ans,"\n\n                                                   Session --",nc,"                                  ")
        elif (op == 11):
            ions = int(input("Please enter the given unit:\n1.Km\n2.Hm\n3.Dm\n4.m\n5.dm\n6.cm\n7.mm\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Km\n2.Hm\n3.Dm\n4.m\n5.dm\n6.cm\n7.mm\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Km\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dm\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"m\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cm\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"mm\n\n                                                    Session --",nc,"                                 ")
        elif (op == 12):
            ions = int(input("Please enter the given unit:\n1.Kl\n2.Hl\n3.Dl\n4.l\n5.dl\n6.cl\n7.ml\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Kl\n2.Hl\n3.Dl\n4.l\n5.dl\n6.cl\n7.ml\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Kl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dl\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"l\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cl\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"ml\n\n                                                    Session --",nc,"                                 ")
        elif (op == 13):
            ions = int(input("Please enter the given unit:\n1.Kg\n2.Hg\n3.Dg\n4.g\n5.dg\n6.cg\n7.mg\n------------>"))
            nons = int(input("\nPlease enter the coverting unit:\n1.Kg\n2.Hg\n3.Dg\n4.g\n5.dg\n6.cg\n7.mg\n------------>"))
            if (ions == 1 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 1 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 1 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 2 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 2 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 3 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 3 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 4 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 4 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*1000
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 5 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 5 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*100
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 6 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 6 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op*10
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 1):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000000)
                nc = nc + 1
                print("The answer is",ans,"Kg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 2):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100000)
                nc = nc + 1
                print("The answer is",ans,"Hg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 3):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10000)
                nc = nc + 1
                print("The answer is",ans,"Dg\n\n                                                   Session --",nc,"                                  ")
            elif (ions == 7 and nons == 4):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/1000)
                nc = nc + 1
                print("The answer is",ans,"g\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 5):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/100)
                nc = nc + 1
                print("The answer is",ans,"dg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 6):
                op = float(input("Enter the value of the given unit: "))
                ans = float(op/10)
                nc = nc + 1
                print("The answer is",ans,"cg\n\n                                                    Session --",nc,"                                 ")
            elif (ions == 7 and nons == 7):
                op = float(input("Enter the value of the given unit: "))
                ans = op
                nc = nc + 1
                print("The answer is",ans,"mg\n\n                                                    Session --",nc,"                                 ")
        elif (op == 14):
            shape = int(input("Please enter the figure: \n1.Circle                        6.trapezoid                     11.hexagon\n2.Square/Rectangle              7.parallelogram                 12.octagon\n3.Triangle                      8.rhombus                       13.annulus\n4.Sector                        9.kite                          14.quadrilateral\n5.Ellipsis                     10.pentagon\n------------->"))
            if (shape == 1):
                pie = 3.14
                r = float(input("Please enter the the value of the radius: "))
                area = float(pie*(r**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 2):
                length = float(input("Please enter the length: "))
                breadth = float(input("Please enter the breadth: "))
                area = float(length*breadth)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 3):
                base = float(input("Please enter the base: "))
                height = float(input("Please enter the height: "))
                area = float(1/2 * base * height)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 4):
                Radius = float(input("Enter the value of the radius: "))
                Angle = float(input("Enter the value of the angle: "))
                area = float((Radius**2)*Angle / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 5):
                large = float(input("Enter the value of the large radius: "))
                small = float(input("Enter the value of small radius: "))
                pie = 3.14
                area = float(pie*large*small)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 6):
                a = float(input("Enter the value of the first parallel line: "))
                b = float(input("Enter the value of the second parallel line: "))
                h = float(input("Enter the height of the trapezoid: "))
                area = float((a + b) * h / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 7):
                h = float(input("Enter the height of the parallelogram: "))
                b = float(input("Enter the base of the parallelogram: "))
                area = float(b*h)
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 8):
                h = float(input("Enter the height of the rhombus: "))
                b = float(input("Enter the base of the rhombus: "))
                area = float(b*h)
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 9):
                e = float(input("Enter the length of the diagonally joined vertical line: "))
                f = float(input("Enter the length of the diagonally joined horizontal line: "))
                area = float((e * f) / 2)
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 10):
                import math
                gg = math.sqrt(5*(5 + 2 * math.sqrt(5)))
                a = float(input("Enter the side of the pentagon: "))
                area = float(1/4 * gg * (a**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 11):
                import math
                gg = math.sqrt(3)
                a = float(input("Enter the length of the side: "))
                area = float(3/2*gg*(a**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 12):
                import math
                gg = math.sqrt(2)
                a = float(input("Enter the length of the side: "))
                area = float(2*(1 + gg)*(a**2))
                nc =  nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 13):
                pie = 3.14
                large = float(input("Enter the radius of the large circle: "))
                small = float(input("Enter the radius of the small circle: "))
                area = float(pie*(large**2 - small**2))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 14):
                e = float(input("Enter the first diagonal length: "))
                f = float(input("Enter the second diagonal length: "))
                a = float(input("Enter the value of angle formed at the intersection of the two diagonals: "))
                area = float(e * f * (180 - a))
                nc = nc + 1
                print("The answer is",area,"\n\n                                                    Session --",nc,"                                 ")
        elif (op == 15):
            shape = int(input("Enter your choice:\n1.sphere                    6.capsule\n2.cube\n3.cone\n4.cylinder\n5.cuboid\n---------------->"))
            if (shape == 1):
                pie = 3.14
                r = float(input("Enter the radius: "))
                v = float((4/3)*pie*(r**3))
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 2):
                a = float(input("Enter the length of the height: "))
                v = float(a**3)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 3):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float((1/3)*pie*(r**2)*h)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 4):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float(pie*(r**2)*h)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 5):
                length = float(input("Enter the length: "))
                breadth = float(input("Enter the breadth: "))
                height = float(input("Enter the height: "))
                v = float(length*breadth*height)
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
            elif (shape == 6):
                pie = 3.14
                r = float(input("Enter the radius: "))
                h = float(input("Enter the height: "))
                v = float(pie*(r**2)*h + (4/3)*pie*(r**3))
                nc = nc + 1
                print("The answer is",v,"\n\n                                                    Session --",nc,"                                 ")
        elif (op == 16):
            t = int(input("Enter your choice: \n1.Celsius --> Fahrenheit            3.Fahrenheit --> Celsius           5.Kelvin --> Celsius\n2.Celsius --> Kelvin                4.Fahrenheit --> Kelvin            6.Kelvin --> Fahrenheit\n\n----------------->"))
            if (t == 1):
                c = float(input("Enter the temperature: "))
                f = float(c*(9/5) + 32)
                nc = nc + 1
                print("The answer is",f,"°F\n\n                                                    Session --",nc,"                                 ")
            elif (t == 2):
                c = float(input("Enter the temperature: "))
                f = float(c + 273.15)
                nc = nc + 1
                print("The answer is",f,"K\n\n                                                    Session --",nc,"                                 ")
            elif (t == 3):
                c = float(input("Enter the temperature: "))
                f = float((c - 32)*5/9)
                nc = nc + 1
                print("The answer is",f,"°C\n\n                                                    Session --",nc,"                                 ")
            elif (t == 4):
                c = float(input("Enter the temperature: "))
                f = float(((c - 32)*5/9) + 273.15)
                nc = nc + 1
                print("The answer is",f,"K\n\n                                                    Session --",nc,"                                 ")
            elif (t == 5):
                c = float(input("Enter the temperature: "))
                f = float(c - 273.15)
                nc = nc + 1
                print("The answer is",f,"°C\n\n                                                    Session --",nc,"                                 ")
            elif (t == 6):
                c = float(input("Enter the temperature: "))
                f = float((c - 273.15) * (9/5) + 32)
                nc = nc + 1
                print("The answer is",f,"°F\n\n                                                    Session --",nc,"                                 ")
        elif (op == 17):
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def print_factors(x):
                print("The factors of", x, "are:")
                for i in range(1, x + 1):
                    if x % i == 0:
                        print(i)
            num = int(input("Enter the number: "))
            print_factors(num)
            print("\n\n========================================================================")
        elif (op == 18):
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def find_prime_factors(n):
                factors = []
                i = 2

                while i * i <= n:
                    if n % i:
                        i += 1
                    else:
                        n //= i
                        factors.append(i)

                if n > 1:
                    factors.append(n)

                return factors


            # Take input from the user
            number = int(input("Enter a number: "))

            # Find prime factors
            prime_factors = find_prime_factors(number)

            # Display the prime factors
            print("Prime Factors of", number, ":")
            print(prime_factors)
            print("\n\n========================================================================")
        elif (op == 19):
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def multiple(m, n):
                a = range(n, (m * n) + 1, n)
                print(*a)
            m = int(input("Enter the number of multiples: "))
            n = int(input("Enter the number: "))
            multiple(m, n)
            print("\n\n========================================================================")
        elif (op ==  20):
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def find_multiples(number, range_start, range_end):
                multiples = []
                for i in range(range_start, range_end + 1):
                    if i % number == 0:
                        multiples.append(i)
                return multiples


            # Take input from the user
            number = int(input("Enter a number: "))
            range_start = int(input("Enter the starting number of the range: "))
            range_end = int(input("Enter the ending number of the range: "))

            # Find multiples within the range
            multiples = find_multiples(number, range_start, range_end)

            # Display the multiples
            print("Multiples of", number, "within the range", range_start, "to", range_end, ":")
            print(multiples)
            print("\n\n========================================================================")
        elif (op == 21):
            import math
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def find_trig_values(angle):
                # Convert angle to radians
                angle_rad = math.radians(angle)

                # Calculate sine, cosine, and tangent
                sine = math.sin(angle_rad)
                cosine = math.cos(angle_rad)
                tangent = math.tan(angle_rad)

                return sine, cosine, tangent


            # Take input from the user
            angle_degrees = float(input("Enter an angle in degrees: "))

            # Find trigonometric values
            sine, cosine, tangent = find_trig_values(angle_degrees)

            # Display the results
            print("Angle:", angle_degrees)
            print("Sine:", sine)
            print("Cosine:", cosine)
            print("Tangent:", tangent)
            print("\n\n========================================================================")
        elif (op == 22):
            import datetime
            nc = nc + 1
            print("\n\n                                                    Session --", nc,
                  "                                 ")
            def calculate_duration(start, end):
                duration = end - start

                years = duration.days // 365
                months = duration.days // 30
                weeks = duration.days // 7
                days = duration.days
                hours = duration.seconds // 3600
                minutes = (duration.seconds // 60) % 60
                seconds = duration.seconds % 60
                milliseconds = duration.microseconds // 1000

                return years, months, weeks, days, hours, minutes, seconds, milliseconds


            # Take input for start and end dates/times
            start_input = input("Enter the start date and time (YYYY-MM-DD HH:MM:SS): ")
            end_input = input("Enter the end date and time (YYYY-MM-DD HH:MM:SS): ")

            # Convert input to datetime objects
            start_date = datetime.datetime.strptime(start_input, "%Y-%m-%d %H:%M:%S")
            end_date = datetime.datetime.strptime(end_input, "%Y-%m-%d %H:%M:%S")

            # Calculate duration
            years, months, weeks, days, hours, minutes, seconds, milliseconds = calculate_duration(start_date, end_date)

            # Display the duration
            print("Duration:")
            print("Years:", years)
            print("Months:", months)
            print("Weeks:", weeks)
            print("Days:", days)
            print("Hours:", hours)
            print("Minutes:", minutes)
            print("Seconds:", seconds)
            print("Milliseconds:", milliseconds)
            print("\n\n========================================================================")
else:
    print(Fore.RED + "!!Wrong password!!")
print(Fore.WHITE + " ")
