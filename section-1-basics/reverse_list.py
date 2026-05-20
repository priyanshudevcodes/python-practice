# Thid function does reverse list whithout using [::-1] or any other list.reverse()
def reverse_list(lst):
    new_lst = []
    for i in range(len(lst)-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst
result = reverse_list([1,2,3,4])
print(result)