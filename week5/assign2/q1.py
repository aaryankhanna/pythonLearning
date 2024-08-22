# traversing the dict and searching for a key

def searchOperation(marks,searchingVal):
    flag=False
    for key in marks.keys():
        if key == searchingVal:
            flag=True
            break
        
    print(flag)




marks = {
    "physics": 80,
    "chemistry": 82,
    "maths": 90,
    "english": 89,
}
valueToBeSearched='English'
searchOperation(marks,valueToBeSearched)