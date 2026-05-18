import random
rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
r_p_s = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:print(rock)
elif user_choice == 1:print(paper)
elif user_choice == 2:print(scissors)
rule = random.randint(0,2)
if user_choice == rule:print(f"Comuter choice:\n{r_p_s[rule]}"),print("Draw")
elif user_choice == 0 and rule == 1:print(f"Computer choice:\n{r_p_s[rule]}"),print("Computer Won!")
elif user_choice == 1 and rule == 2:print(f"Computer choice:\n{r_p_s[rule]}"),print("Computer Won!")
elif user_choice == 2 and rule == 1:print(f"Computer choice:\n{r_p_s[rule]}"),print("You Won!")
elif user_choice == 1 and rule == 0:print(f"Computer choice:\n{r_p_s[rule]}"),print("You Won!")
elif user_choice == 2 and rule == 0:print(f"Computer choice:\n{r_p_s[rule]}"),print("Computer Won!")
elif user_choice == 0 and rule == 2:print(f"Computer choice:\n{r_p_s[rule]}"),print("You Won!")
