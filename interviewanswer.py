import random

for row in range(1,13):
    for col in range(1,13):
        print(row*col, end="\t")
    print()

def whatever(x):
    while x > 0:
        suit = random.randint(1,4)
        card = random.randint(1,13)
        if card == 11:
            card = "Jack"
        elif card == 12:
            card = "Queen"
        elif card == 13:
            card = "King"

        if suit == 1:
            suit = "Spade"
        elif suit == 2:
            suit = "Heart"
        elif suit == 3:
            suit = "Diamons"
        elif suit == 4:
            suit = "Club"
        thing = card,"of",suit
        cardlist.append(thing)
        x -= 1

if __name__ == "__main__":
    print ("Connor Mitchell")
    cardlist = []
    x = int(input("How many cards: "))
    whatever(x)
    print (cardlist)
