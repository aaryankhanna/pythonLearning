def isPallindrome(string):
    newString = string[::-1]
    print(newString)
    if (newString == string):
        return True
    else:
        return False


print(isPallindrome("moom"))
