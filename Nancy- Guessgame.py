import random
answer = random.randint(1, 50)

print(answer)

turns_left = 5

guess = input("what is your guess?")

while turns_left > 0:

    if guess == str(answer):
        print("You win!")
        quit()

    elif guess < str(answer):
        print("Guess higher")
        guess = input("What is your guess?")
        turns_left -= 1
    elif guess > str(answer):
        print("Guess lower")
        guess = input("What is your guess?")
        turns_left -= 1

if turns_left == 0:
        print("You lose")
        quit()