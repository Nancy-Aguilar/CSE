import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

print("Welcome to lucky 7's!")
print("You start off with 15 dollars and each round is 1 dollar")
print("If you roll a 7 in a round you get 4 dollars plus the 1 dollar you used to play")
print("If you don't roll a 7 you lose the dollar you used to play")
print("Have fun!")

money = 15
total = dice1 + dice2


while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)


if total > 7:
    print("You lose")

if roll < 7:
    print("You lose")

if roll == 7:
    print("You win")
    money += 5
    print("Your current amount is now %s" % money)