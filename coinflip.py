import random

print("Welcome to the Coin Flipper! Flip a coin and get a random result!")
numFlips = int(input("How many coins do you want to flip?: "))

count = 0

while count < numFlips:
    flip = random.randint(1, 2)
    if flip == 1:
        print("The flip is 'Head'")
    else:
        print("The flip is 'Tails'")
    count += 1