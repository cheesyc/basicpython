import random
howmany = int(input("How many times do you want the coin to be flipped: "))
outcomes = []
while howmany > 0:
    num = random.randint(1,2)
    outcomes.append(num)
    howmany -=1
lis = []
for i in outcomes:
    if i == 1:
        lis.append("Tails")
    if i == 2:
        lis.append("Heads")
print (lis)
