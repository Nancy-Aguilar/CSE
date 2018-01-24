import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "No precious jewel can be compared to you", "A blue rose", "Double rainbow"]

word = random.choice(word_bank)

str1 = word
listOne = list(str1)
print(listOne)

guesses_left = 10
letters_guessed = []

while guesses_left > 0:
    guesses_left -= 1
    guess = input("What is your guess?")
    letters_guessed.append(guess)

