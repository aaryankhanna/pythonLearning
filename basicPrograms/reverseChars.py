# reversing characters of words in a string

string = "python is good"
newList = []
myList = string.split()
for i in range(len(myList)):
    newList.append(myList[i][::-1])

newString = " ".join(newList)
print(newString)
