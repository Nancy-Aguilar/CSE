import random
answer = random.randint(1, 50)

print(answer)

guess = int(input("what is your guess?"))

turns_left = 5

correct_guess = True


if turns_left > 0 and correct_guess == True:
    if guess == answer:
        print("You win!!!")
        quit()

correct_guess = False

if turns_left > 0 and correct_guess == False:
    if guess > answer:
        print("It's too high guess lower.")
        guess = input("Guess again")

    elif guess < answer:
        print("Its too low guess higher")
        guess = input("Guess again")
        