while True:
    try:
        number = int(input("Enter you first number:"))
        number_2 = int(input("Enter your second number:"))
        operation_perform = input("Enter the operation you wanna perform(eg:+,-,*,/,%)")
        match operation_perform:
            case "+": print(number+number_2)
            case "-":print(number-number_2)
            case "*":print(number*number_2)
            case "/":print(number/number_2)
            case "%":print(number%number_2)
    except ValueError:
        print("Inter valid values")
    except ZeroDivisionError:
        print("Can't be divisible by zero")