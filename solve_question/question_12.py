# Create a number guessing game. 
import random

hidden_number = random.randint(1,50)
print("Welcome to The number guessing game")
print("The guessing number 1 to 50")

while True:
    num = int(input("Please Enter a number: "))
    if num < hidden_number:
        print("Too Low! Try again.")
    elif num > hidden_number:
        print("Too high! Try again")
    else:
        print(f"Congratulation! You Guessed it right.")
        break