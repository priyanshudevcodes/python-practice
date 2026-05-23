import random
from rich import print
print(r"""_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/""")
print("[bold yellow]You only have 6 lives...... to play[/bold yellow]")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
def world_list(w_l):
    choosen_world = random.choice(w_l)
    return choosen_world
result_1 = world_list(w_l=["gamer","master","worker","animal"])
correct_letters = []
game_over = False
lives = 6
while not game_over:
    guess = input("Guess the word:").lower()
    place_holder = ""
    for position in range(len(result_1)):
        place_holder += "_"
    display = ""
    for result in result_1:
        if result == guess:
            display += result
            correct_letters.append(guess)
        elif result in correct_letters:
            display += result
        else:
            display += "_"
    print(display.replace(""," ").strip())
    if "_" not in display:
        game_over = True
        print("[bold green]You Won!![/bold green]")
    if guess not in result_1:
        lives -= 1
        if lives == 0:
            game_over = True
            print("[bold red]You lose...[/bold red]")
            print(f"[bold green][bold red]The answer is[/bold red] {result_1}[/bold green]")
    print(stages[lives])