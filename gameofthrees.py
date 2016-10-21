num = int(input("Number: "))
count = 0
while num != 1:
    if num % 3 == 0:
        print (num,"/3")
        num /= 3
        count += 1
    elif num <= 0:
        print (num,"+1")
        num += 1
        count += 1
    else:
        print (num,"-1")
        num -= 1
        count += 1
print ("Finished in ",count,"turns")
