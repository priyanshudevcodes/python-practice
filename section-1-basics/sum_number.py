number = input("Enter your number:")
set_func = [f for f in str(number)]
rule_to_show = "+".join(set_func)
rule_for_total = sum(int(num_in_func) for num_in_func in set_func)
print(f"The number {number} has total sum is {rule_to_show} = {rule_for_total}")