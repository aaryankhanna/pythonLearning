# remove duplicates in string

def removeDuplicates(string):
    result = []
    for i in range(len(string)):
        if string[i] not in result:
            result.append(string[i])
    result = "".join(result)
    return result


print(removeDuplicates("hheeelllooo"))
