import random

# Generate a random number between 1 to 10
secret_number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 to 10: "))

# Check the guess
if guess == secret_number:
    print("Congratulations! You guessed correctly")
elif guess < secret_number:
    print("You guessed too low.\nSecret number was:", secret_number)
elif guess > secret_number:
    print("You guessed too high.\nThe secret number was:", secret_number)