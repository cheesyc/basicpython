import math
side1 = float(input("Input length of side 1: "))
side2 = float(input("Input length of side 2: "))
hype = float(input("Input length of the hypotonus: "))

side1tru = side1 ** 2
side2tru = side2 ** 2

equals = math.sqrt(side1tru + side2tru)

if equals == hype:
    print ("It is a Pythagarian Triple")
else:
    print ("Not a Pythagarian Triple")
