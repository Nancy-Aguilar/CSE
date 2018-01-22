import random
word_bank = ["Diamond", "Believe in yourself", "Pusheen the cat", "Space unicorn", "Chocolate", "Tiger", "Friendship",
             "No precious jewel can be compared to you", "A blue rose", "Double rainbow"]

word = random.choice(word_bank)

str1 = word
listOne = list(str1)
print(listOne)

guess = input("What is your guess?")

if guess == word:
    print("You win!")