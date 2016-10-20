import random

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
            suit = "Spades"
        elif suit == 2:
            suit = "Hearts"
        elif suit == 3:
            suit = "Diamons"
        elif suit == 4:
            suit = "Clubs"
        thing = card,"of",suit
        cardlist.append(thing)
        x -= 1

if __name__ == "__main__":
    print ("Connor Mitchell")
    for row in range(1,13):
        print(*("{:3}".format(row*col) for col in range(1, 13)))
    cardlist = []
    x = int(input("How many cards: "))
    whatever(x)
    print (cardlist)
