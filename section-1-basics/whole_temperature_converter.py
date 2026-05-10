while True:
    user_temperature = int(input("Enter your temperature: "))
    temp_unit = float("Enter your unit name[Kelvin:- K,Celsius:- C , Fehrenheit:- F]: ")
    if temp_unit == "K":
        unit_F = user_temperature*9/5-459.67
        unit_C = user_temperature-273.15
        print(f"{user_temperature}°K:- {unit_C}°C and {unit_F}°F")
    elif temp_unit == "C":
        unit_f_1 = user_temperature*1.8 + 32
        unint_K =user_temperature+273.15
        print(f"{user_temperature}°C:- {unint_K}°K and {unit_f_1}°F")
    elif temp_unit == "F":
        unit_c_1 = (user_temperature-32)/(9/5)
        unit_k_1 = (user_temperature + 459.67) * 5/9 
        print(f"{user_temperature}°F:- {unit_c_1}°C and {unit_k_1}°K")
    else:
        print("Invalid unit! Enter K, C or F only.")