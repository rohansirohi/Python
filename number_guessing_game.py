import random

secret_number = random.randint(1, 10)
attempts = 3

print("I'm thinking of a number between 1 and 10")

while attempts > 0:
  guess = int(input("Take a Guess: "))
  if guess == secret_number:
    print("Congrats, you guesssed the number")
    break
  elif guess < secret_number:
    print("Too low, try again.")
  else:
    print("Too high, try again.")
  attempts -= 1

  if attempts == 0:
    print("Sorry, you run out of attempts. The number was: ", secret_number)
