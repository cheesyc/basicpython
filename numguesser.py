import random
while True:
    num = random.randint(1,100)
    while True:
        guess = int(input("Guess a number out of 100: "))

        if num == guess:
            again = str.lower(input("Correct! Want to try again?(y/n): "))
            if again == "y":
                break
            else:
                raise SystemExit
            break
        if num > guess:
            print ("Close! The number is larger than your guess")
        elif num < guess:
            print ("Close! The number is smaller than your guess")
