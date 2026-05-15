import datetime
from birthday_cake import show_birthday_cake
def dob_calculator(birthdate):
    today = datetime.date.today()
    time_difference = today - birthdate
    age = time_difference.days // 365.2425
    return int(age)
dob = datetime.date(int(input("Enter which year you born>>> ")),int(input("Enter which month you born[don't use 0 in first place]>>> ")),int(input("Enter which day you born in[don't use 0 in first place]>>> ")))
name = input("Enter your unique name: ")

if datetime.date.today().month == dob.month and datetime.date.today().day == dob.day:
    show_birthday_cake(name)
else:
    print(f"Name:{name}\nAge:{dob_calculator(dob)} years old")
    