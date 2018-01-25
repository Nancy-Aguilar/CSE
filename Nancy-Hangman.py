import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "No precious jewel can be compared to you", "A blue rose", "Double rainbow"]

word = random.choice(word_bank)
str1 = word
listOne = list(str1)
guesses_left = 10
letters_guessed = []

for letter in listOne:
    print("*")

while guesses_left > 0:
    guesses_left -= 1
    guess = input("What is your guess?")
    letters_guessed.append(guess)

    if guess == listOne[0]:
        print("Yay")

    if guess == word:
        print("You win!")
        quit()