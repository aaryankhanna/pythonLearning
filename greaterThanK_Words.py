# Print all the words which are greater or equal to k.
def greaterThanWords(sentence, k):
    myList = sentence.split()
    result = []
    print(myList)
    
    for word in myList:
        if len(word) >= k:
            result.append(word)
    result = " ".join(result)
    return result


sentence = "python is great language. very easy to understand."
k = 5
print(greaterThanWords(sentence, k))
