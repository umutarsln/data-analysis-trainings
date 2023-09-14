
myDict = {}

for i in range(10):
    if i % 2 == 0:
        myDict[i] = i**2
    else:
        myDict[i] = i


print(myDict)


newDict = {n: n**2 for n in range(10) if n % 2 == 0}

print(newDict)