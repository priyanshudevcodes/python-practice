
while True:
    Number = int(input("Enter your number:"))
    try:
        if Number%2==0:
            print(f"{Number} is an 'Even Number'") 
        elif Number==0:
            print(f"{Number} is an 'Even Number")
        elif Number%2!=0:
            print(f"{Number} is an 'Odd Number'")
    except Exception as e:
        print(e)
        break