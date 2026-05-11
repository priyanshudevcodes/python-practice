n = int(input("Enter the your value of (n!): "))
r = int(input("Enter the your value of (r!): "))

def factorial(num):
    if num < 0:
        return "Not exist with negative numbers"
    result = 1
    for x in range(1,num+1):
        result *= x
    return result
combination_formula = factorial(n)/(factorial(r)*factorial(n-r))
print(combination_formula)
        