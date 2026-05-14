# Tells the name of the student who got second last marks
import heapq
while True:
    storre_data = []
    for i in range(int(input("Enter the number of students: "))):
        n = input("Enter the name of the student: ")
        score = float(input("Enter the score of that student: "))
        new = [n,score]
        storre_data.append(new)
    rule = heapq.nsmallest(2,storre_data,key=lambda x:x[0])
    second_lowest = rule[1][1]
    for student in storre_data:
       if student[1] == second_lowest:
            print(student[0])
