word = input("Word: ")
lis = []
lis.append(word)
list(lis)
count = len(word)
vowelc = 0
vowell = ['a','e','i','o','u']
for i in range(0, count):
    if lis[i] == vowell:
        vowelc += 1
print (vowelc)
