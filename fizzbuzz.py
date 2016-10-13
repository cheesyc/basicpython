def fizz(num):
    if num % 3 == 0:
        return True
    else:
        return False
def buzz(num):
    if num % 2 == 0:
        return True
    else:
        return False
while True:
    num = int(input("Number: "))

    if fizz(num) and buzz(num) == True:
        print ("Fizzbuzz!")
    elif fizz(num) == True:
        print ("Fizz!")
    elif buzz(num) == True:
        print ("Buzz!")
    else:
        print ("Neither")

    again =  str.lower(input("Do you want to go again?(y/n): "))

    if again == "n":
        raise SystemExit
