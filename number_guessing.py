import random

number = random.randint(1, 100)
guess = None

print("Guess a number between 1 and 100:")

while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("🎉 Correct! The number was", number)