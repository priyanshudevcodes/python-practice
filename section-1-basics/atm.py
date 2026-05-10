Total_balance = 10000
user_pin = int(input("Enter the pin: "))
pin = 1235897
if user_pin==pin:
        print(f"Total balance:- {Total_balance}")
elif user_pin!=pin:
     print("Access Denied")
while True:
    press = input("Enter X to start for Deposit and Y for Withdraw and E to exit:- ")
    if press=="X":
        deposit = int(input("Enter the amount you want to be deposit: "))
        Total_balance = Total_balance+deposit
        print(f"Total balance:- {Total_balance}\nTotal Deposites:- {deposit}")
    elif press=="Y":
         widhraw = int(input("Enter the amount you want to be withdrew: "))
         if widhraw > Total_balance:
            print("invalid")
         else:
              print(f"{Total_balance-widhraw}")
    elif press=="E":
        print("Next Time!!")
        break
    
