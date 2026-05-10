
list = []
for i in range(10):
    rule = int(input(f"Enter your number {i+1}: "))
    list.append(rule)
total = 0
for n in list:
    total+=total+n
average = total/len(list)
print(f"The average is {average}")
maximum = list[0]
for n in list:
    if n>maximum:
        maximum = n
print(f"The maximum number is {maximum}")
minimum = list[0]
for n in list:
    if n<minimum:
        minimum=n
print(f"The minimum number is {minimum}")