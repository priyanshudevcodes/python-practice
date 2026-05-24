import itertools
# Marks of two students in mathematics of two semesters
marks_list = [("Rahul", 42),("Rahul", 70),("John", 86),("John", 58)]

# Key function
key_func = lambda x:x[0]

for key,group in itertools.groupby(marks_list,key_func):
    print(f"{key} : {list(group)}")