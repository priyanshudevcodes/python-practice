import random
user_enter = input("Enter [X] to start the number guessing game: ")
if user_enter =="X":
    rule = random.randint(1,100)
count = 0
while True:
    user_answer = input("Enter your answer[type only 1-100 numbers]: ")
    if user_answer=="I quit":
        print(f"Good luck for next time.The answer is {rule}")
        break
    user_answer=int(user_answer)
    if rule==user_answer:
        print(f"Correct you won a Car!!!!")
        break
    if rule != user_answer:
        if user_answer>rule:
            print("High")
        elif user_answer<rule:
            print("low")
    for i in str(user_answer):
        count+=1
        print(count)
  