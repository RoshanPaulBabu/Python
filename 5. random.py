import random
num = random.randrange(10,99)

while True:
    guess = int(input("Guess a number"))
    if guess > num:
        print("Too High")

    elif guess < num:
        print("Too Low")

    else:
        print("Your guess is right")
        break
        

