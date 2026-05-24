from itertools import chain,accumulate
number_list_1 = [2,4,8,16]
number_list_2 = [3,9,27,84]
number_list_3 = [4,16,64,256]
number_list_4 = [5,25,125,625]
number_list_5 = [6,36,216,1296]
result_number_list = list(chain(number_list_1,number_list_2,number_list_3,number_list_4,number_list_5))
print(list(accumulate(result_number_list)))