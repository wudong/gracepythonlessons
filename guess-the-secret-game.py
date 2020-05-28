import random
secret = random.randrange(22, 222)
guess = 0
tries = 0
while guess != secret:
    guess = int(input("make a guess: "))
    tries = tries + 1
    if guess > secret:
        print("your guess is to high!!")
    elif guess < secret:
        print("you guess is to low!!")
    else:
        print("your guess is just right!!")
print("number of tries",tries)

