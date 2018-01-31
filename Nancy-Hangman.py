import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "Puglie the pug", "A blue rose", "Double rainbow"]
word = random.choice(word_bank)
str1 = word
word_list = list(str1)
guesses_left = 10
letters_guessed = []

while guesses_left:
    for letter in word_list:
        print("*")
    guess = input("What is your guess?")
    letters_guessed.append(guess)

    if guess in word_list:
        print("Yay")

    if guess not in word_list:
        guesses_left -= 1

