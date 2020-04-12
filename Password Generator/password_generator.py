'''This Python code generates a random password for the user.
It asks the user how long the password should be, and how many
letters and numbers the password should contain. Then it generates
the password which contains mixture of lowercase and uppercase letters,
numbers and special symbols. It also checks for ValueError and invalid
inputs. The minimum length of password should be 6 chars long.
'''
import random
def generate_password():
    s_letters="abcdefghijklmnopqrstuvwxyz"
    c_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums="0123456789"
    s_symbols="!@#$%^&*"
    password=[]
    try:
        length=int(input("Enter length of your password(minimum 6 chars long): "))
        if length<6:
            print("Couldn't generate. Length should be minimum 6 chars long.")
            return
        letters=int(input("Enter how many letters? "))
        if letters>length:
            print(f"Couldn't generate. No of letters should be less than {length}")
            return
        numbers=int(input(f"Enter how many numbers? {length-letters} chars remaining "))
        if numbers>(length-letters):
            print("Couldn't generate. Total no exceeds the given length.")
            return
        for i in range(letters):
            if i%2==0:
                password.append(s_letters[random.randint(0,25)])
            else:
                password.append(c_letters[random.randint(0,25)])
        for i in range(numbers):
            password.append(nums[random.randint(0,9)])
        remaining=length-(numbers+letters)
        for i in range(remaining):
            password.append(s_symbols[random.randint(0,7)])
        random.shuffle(password)
        password = "".join(password)
        print(f"Your generated password is : {password}")
    except ValueError:
        print("Couldn't generate. Not a valid number.")
        return
generate_password()

