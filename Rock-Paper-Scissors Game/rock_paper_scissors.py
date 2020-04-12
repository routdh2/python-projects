'''Program to implement Rock,Paper,Scissors game in Python'''
import random

def start_game():
    choice=["Rock","Paper","Scissors"]
    while True:
        computer=choice[random.randint(0,2)]
        player=input("Rock/Paper/Scissors ?")
        player=player.lower()
        if player==computer.lower():
            print("It's a tie.")
        elif player=="rock":
            if computer=="Paper":
                print(f"You lose! {computer} covers {player}")
            else:
                print(f"You win! {player} smashes {computer}")
        elif player=="paper":
            if computer=="Rock":
                print(f"You win! {player} covers {computer}")
            else:
                print(f"You lose! {computer} cuts {player}")
        elif player=="scissors":
            if computer=="Rock":
                print(f"You lose! {computer} smashes {player}")
            else:
                print(f"You win! {player} cuts {computer}")
        else:
            print("Invalid input. Check your spellings.")
        option=input("Do you want to continue...(Y/N)")
        if option.lower()=="y":
            continue
        else:
            break

start_game()

