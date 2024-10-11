import random

# welcome section
print("hey, welcome to my game")
welcome=input("do you want to play 'snake water gun' ?\n" "").lower()
if welcome == "yes":
    print("lets begin!!")
else:
    print("no problem")
    exit()

# explaining the game
print("let me explain you the rules first")
print("you have to choose between 3 characters of this game, which are:\nsnake,water and gun")
print("the snake beats water\nthe gun beats the snake\nthe water beats the gun\n" "")
start=input("are you ready ?").lower()
if start == "yes":
    print("lets begin!!")
else:
    print("no problem")
    exit()

#taking input
while True:
    characters=["snake","water","gun"]
    print("make your decision!!")
    choose=input("snake, water or gun?\n").lower()
    random_choice=random.choice(characters)
    print("computer's choice:",random_choice)

    #win or loose
    if choose == random_choice:
        print("It's tie!")
    elif choose=="snake" and random_choice=="water":
        print("you won!")
    elif choose=="water" and random_choice=="gun":
        print("you won!")
    elif choose=="gun" and random_choice=="snake":
        print("you won!")
    else:
        print("sorry, you loose!!")
        
    #play again
    play_again=input("do you want to play again ? (yes/no)").lower()
    if play_again != "yes":
        print("thanks for playing!")
        break





