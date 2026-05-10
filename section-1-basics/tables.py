while True:
    try:
        number = int(input("Enter a number between 1 to 10:"))
        if 1<=number<=10:
            print("Enter a valid values within the range")
            for i in range(1,11):
                 print(f"{number} X {i} = {i*number}")
    except Exception as e:
        print(e)
        break