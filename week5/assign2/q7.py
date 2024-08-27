# returning even values from the list of values in dictionary

def evenValFromList(d1):
    for key, val in d1.items():
        evenList = list()
        for i in range(len(val)):
            if (val[i] % 2 == 0):
                evenList.append(val[i])
        d1[key] = evenList
    print(d1)
    


d1 = {
    "A": [1, 2, 3, 4],
    "B": [5, 6, 7, 8]
}
evenValFromList(d1)
