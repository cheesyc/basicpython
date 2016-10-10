word = input("What word do you want checked?: ")

reverse = word[::-1]

if word == reverse:
    print ("It is a palindrome")
else:
    print ("It isn't a palindrome")
