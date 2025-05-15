def largestEle(arr):
    maxEle=arr[0]
    for i in range(1,len(arr)):
        maxEle = max(maxEle,arr[i])
    return maxEle


arr = [1, 8, 700, 56, 90]
print(largestEle(arr))