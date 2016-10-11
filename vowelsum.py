word = input("Word: ")
trulist = list(word)
count = len(trulist)
vowelc = 0
vlist = []
i = 1
while i < count:
    if trulist[i] == "a":
        vowelc += 1
        vlist.append("a")
        i += 1
    elif trulist[i] == "e":
        vowelc += 1
        vlist.append("e")
        i += 1
    elif trulist[i] == "i":
        vowelc += 1
        vlist.append("i")
        i += 1
    elif trulist[i] == "o":
        vowelc += 1
        vlist.append("o")
        i += 1
    elif trulist[i] == "u":
        vowelc += 1
        vlist.append("u")
        i += 1
    else:
        i += 1
print (vowelc,"amount of vowels. The vowels in the word are",vlist)
