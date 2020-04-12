'''Python application for 'Guess the Number' game'''
import random

class Application:

    def __init__(self, start=0, end=20):
        self.start=start
        self.end=end
        self.computer=random.randint(self.start,self.end)
    def start_game(self):
        while True:
            try:
                user_guess=int(input(f"Guess the number between {self.start} to {self.end}..."))
                if self.computer==user_guess:
                    print("Congratulations!! You have guessed it right.")
                    break
                elif user_guess<self.start or user_guess>self.end:
                    print(f"{user_guess} is not in range.")
                elif user_guess<self.computer:
                    print(f"{user_guess} is too low!")
                else:
                    print(f"{user_guess} is too high!")
                option=input("Do you want to continue...(Y/N)")
                if option.lower()=='y':
                    continue
                else:
                    break
            except (KeyboardInterrupt, ValueError) as e:
                print("Oops! The input is not valid.")
                break

# app=Application()
# app.start_game()
