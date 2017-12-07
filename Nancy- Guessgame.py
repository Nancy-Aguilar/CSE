import random
answer = random.randint(1, 50)

guess = int(input("what is your guess?"))

turns_left = 5

correct_guess = False

if turns_left > 0 and correct_guess == False:
    if guess == answer:
        print("You win!!!")
    elif guess > answer:
        print("It's too high guess lower.")
