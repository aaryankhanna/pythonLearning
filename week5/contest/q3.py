# convert string to uppercase if 2/first 4 characters is in uppercase

def checkUpper(string):
    count = 0
    for i in range(0, 4):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            count += 1
    if count >= 2:
        print(string.upper())
    else:
        print(string)


string = "HelLo"
checkUpper(string)
