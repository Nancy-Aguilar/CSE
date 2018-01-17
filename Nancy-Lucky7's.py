import random

print("Welcome to lucky 7's!")
print("You start off with 15 dollars and each round is 1 dollar")
print("If you roll a 7 in a round you get 4 dollars plus the 1 dollar you used to play")
print("If you don't roll a 7 you lose the dollar you used to play")
print("Have fun!")

money = 15
rounds = 0
while money > 0:
    money -= 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Your current amount is now %s" % money)
    print("You rolled a %s" % dice1)
    print("You rolled a %s" % dice2)
    print("Your total is %s" % total)
    if total == 7:
        rounds += 1
        money += 5
        print("You won")
        print("Your current amount is now %s" % money)
    if total > 7:
        rounds += 1
        print("You lost")
    if total < 7:
        rounds += 1
        print("You lost")
    if money == 0:
        print("Game over, you have no money left to continue playing")
        print("You played %s rounds" % rounds)