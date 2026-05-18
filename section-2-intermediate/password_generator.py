import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
new_list = []
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
letter = random.choices(letters,k=nr_letters)
number = random.choices(numbers,k=nr_numbers)
symbol = random.choices(symbols,k=nr_symbols)
for i in range(nr_letters):
    rule = random.choice(letter)
    rule_1 = random.choice(number)
    rule_2 = random.choice(symbol)
    new_list.append(rule)
    new_list.append(rule_1)
    new_list.append(rule_2)
print(new_list)
random.shuffle(new_list)
result = "".join(new_list)
print(result)