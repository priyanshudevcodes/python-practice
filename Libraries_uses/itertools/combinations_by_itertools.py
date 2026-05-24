from itertools import combinations, combinations_with_replacement
numbers_1 = [1,2,3,4,5,6]

# without replacement order doesn't matter , no repeats
without_replacements = list(combinations(numbers_1,3))

# with replacement elements can repeat
with_replacements = list(combinations_with_replacement(numbers_1,3))
print(f"Combinations without replacement : {without_replacements}")
print(f"Combinations with replacement : {with_replacements}")