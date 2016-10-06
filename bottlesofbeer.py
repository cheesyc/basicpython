ready = input("Ready?(y/n): ")

if ready == "y":
    bottels = 99
    while bottels > 0:
        print (bottels, "of beer on the wall!",bottels,"bottels of beer!")
        bottels -=1
        print ("Take one down! Pass it around!",bottels,"of bear on the wall!")
