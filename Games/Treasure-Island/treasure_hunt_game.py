import art
import keeper
print(art.logo)
print("Welcome to the Treasure Island.\nYour mission is to find treasure.")
path_choose = input("Your at a cross road where do you want to go?\n    Type 'left' or 'right'\n")
if path_choose == "right":
    print("You fell into a hole.")
    print(art.hole)
    print(art.game_over)
elif path_choose.lower() == "left":
    rule = input("You have come to a lake. There is an island in the middle of the lake.\n  Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if rule.lower() == "swim":
        print("You get attack by an angry trout.")
        print(art.game_over)
    elif rule.lower() == "wait":
        print(art.scene) 
        step_2 = input("You arrive at the island unharmed.There is the housr with 3 doors\n  one red, one yellow, one blue . Which color do you choose?\n")
        if step_2.lower() == "red":
            print("It's a room full of fire.")
            print(art.game_over)
        elif step_2.lower() == "yellow":
            print("You found the treasure!!!!")
            print(art.win)
        elif step_2.lower() == "blue":
            print("You enter a room full of beasts.")
            print(art.beast)
            print(art.game_over)
elif path_choose.lower() == "leftright":# To start the secret word first enter leftright into first input where ask for direction
    keeper.run_keeper() # secret word is Priyanshuisbest (You can change whatever you want it's just a demo)