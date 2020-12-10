import random

print("Number guessing game")

number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:

    guess = int(input("Your guess: "))

    if guess == number:
        print("Congratulations! YOU Win!!!")
        exit()

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances = chances+1


if chances >= 5:
    print("You Lost! Try again next time. The correct number is", number)