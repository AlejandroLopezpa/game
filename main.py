from replit import clear
import random

win = """

██    ██  ██████  ██    ██     ██     ██ ██ ███    ██        ██  
 ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██     ██  ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██         ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██     ██  ██ 
   ██     ██████   ██████       ███ ███  ██ ██   ████        ██                                                     
"""

lost = """

"""
logo = """
 ██████   █████  ███    ███ ███████     ██████   █████  ██████  ████████  ██████      
██       ██   ██ ████  ████ ██          ██   ██ ██   ██ ██   ██    ██    ██    ██     
██   ███ ███████ ██ ████ ██ █████       ██████  ███████ ██████     ██    ██    ██     
██    ██ ██   ██ ██  ██  ██ ██          ██   ██ ██   ██ ██   ██    ██    ██    ██     
 ██████  ██   ██ ██      ██ ███████     ██████  ██   ██ ██   ██    ██     ██████      
"""
lives = ""

levels = {
        "Easy" : 12,
        "Medium" : 8,
        "Hard" : 4,
        }
numer =  range(1,100)
number_random = random.choice(numer)

def play():
    play = input("Do you want to play again? 'y' or 'n': ")
    if play == "y":
        clear()
        game()
    elif play == "n":
        print("bye")

def game():
    print(logo)
    for _ in levels:
        print(f"Level {_}")
    chosen_level = input("Pick a level: ")
    game_level = levels[chosen_level]
    while game_level != 0:
        score = int(input("Pick a number bewteen 1 and 100: "))
        if score == number_random:
            print(win)
            play()
        elif score < number_random:
            print(f"The number {score} is greater")
        elif score > number_random:
            print(f"The number {score} is less")
        game_level -= 1
        print(f"Your lives {game_level}")

    else:
            print(f"You lost the number is {number_random}.")
            play()

if __name__ == '__main__':
    game()

