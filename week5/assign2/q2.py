# merging dictionaries

def mergingDicts(d1, d2):
    for key, value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value
    print(d1)


d1 = {
    "apple": 3,
    "banana": 5,
    "cherry": 7
}
d2 = {
    "banana": 8,
    "orange": 10,
    "apple": 9
}
mergingDicts(d1, d2)
