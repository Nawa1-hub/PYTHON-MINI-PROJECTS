import random

secret_number = random.randint(1, 50)
attempts = 0
guess = 0

print("Welcome to the Guess-the-Number Game! 🎯")
print("I'm thinking of a number between 1 and 50.")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempts.")
    except ValueError:
        print("Invalid input. Please enter a number.")
