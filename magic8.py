import random
from time import sleep
question = input("What is your question?: 1")
number = random.randint(1,7)

print ("Hmmm...thinking")
sleep(5)

if number == 1:
    print ("Yes")
elif number == 2:
    print ("No")
elif number == 3:
    print ("Maybe")
elif number == 4:
    print ("It's probable")
elif number == 5:
    print ("It doesn't look likely")
elif number == 6:
    print ("Ask again later")
elif number == 7:
    print ("Not sure")
