import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "Puglie the pug", "A blue rose", "Double rainbow"]
word = random.choice(word_bank)

guesses_left = 10

letters_guessed = []

while guesses_left:
    output = []
    guess = input("What is your guess?")
    letters_guessed.append(letter)
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    output = ''.join(letter)
    print(output)