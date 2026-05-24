from itertools import product
sizes_set = {"S","M","L"}
color_set = {"red","blue","green"}
cartisan_product = set(product(sizes_set,color_set))
print(cartisan_product)