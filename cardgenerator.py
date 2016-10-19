import random
from prettytable import PrettyTable
countdown = 12
multiples2 =
t = PrettyTable([])
multiples = [1,2,3,4,5,6,7,8,9,10,11,12]

while countdown > 0:
    for i in multiples:
        for x in multiples:
            t.add_row([i * multiples[x]])
    countdown -= 1

club = random.randint(1,4)
card = random.randint(1,13)

if card == 11:
    card = "Jack"
elif card == 12:
    card = "Queen"
elif card == 13:
    card = "King"
if club == 1:
    club 
if __name__ == __main__:
    print ("Connor Mitchell")
    print (t)
