import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "No precious jewel can be compared to you", "A blue rose", "Double rainbow"]

word = random.choice(word_bank)

str1 = word
listOne = list(str1)
print(listOne)

guesses_left = 10

while guesses_left > 0:
    letters_guessed = [input("What is your guess?")]
    guesses_left -= 1


    if letters_guessed == word:
        print("You win!")
        quit()

    if guesses_left == 0:
        print("You have no guesses left")