def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    leftSide=arr[:mid]
    rightSide= arr[mid:]
    LS=mergeSort(leftSide)
    RS=mergeSort(rightSide)
    return merge(LS,RS)



arr=[1,7,2,8,4,6,7,9,2,1,5,9,54,3,4,5]
print(mergeSort(arr))

