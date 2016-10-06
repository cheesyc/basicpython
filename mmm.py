howmany = input("How many numbers are you using?: ")
count = howmany
num = []

while count > 0:
    for i in howmany:
        x = input("Insert number ",i,": ")
        num.append(x)
        count -= 1

def sort(num):
    size = len(num)
    for i in range(size):
        for j in range(size-i-1):
            if(num[j] > num[j+1]):
                tmp = num[j]
                num[j] = num[j+1]
                num[j+1] = tmp
    return num

srted = sort(num)

def mean (num):
    mean = sum(num)/howmany
    return mean

def median (srted):
    return srted((howmany + 1)/2)

def mode (num):
    
