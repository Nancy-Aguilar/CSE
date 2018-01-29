import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "No precious jewel can be compared to you", "A blue rose", "Double rainbow"]

word = random.choice(word_bank)
str1 = word
word_list = list(str1)
guesses_left = 10
letters_guessed = []

for letter in word_list:
    print("*")

while guesses_left > 0:
    guesses_left -= 1
    guess = input("What is your guess?")
    letters_guessed.append(guess)

    if guess == word_list[0]:
        print("Yay")