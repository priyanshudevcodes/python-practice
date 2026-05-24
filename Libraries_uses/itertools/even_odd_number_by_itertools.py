from itertools import count,islice
# For getting first 20 even numbers
rule = (count(start=0,step=2))
result = list(next(rule)for i in islice(range(40),20))
print(f"Even numbers : {result}")
# For getting first 20 odd numbers
rule_2 = (count(start=1,step=2))
result_2 = list(next(rule_2)for _ in islice(range(40),20))
print(f"Odd numbers : {result_2}")