# def sortedNdRotated(arr):
#     temp=arr[::]
#     temp.sort()
#     check=[]
#     index=temp.index(arr[0])
#     for i in range(index,len(temp),1):
#         check.append(temp[i])
#     for i in range(0, index,1):
#         check.append(temp[i])
#     if check== arr:
#         print(True)
#     else:
#         print(False)
        
    
# sortedNdRotated([2,1,3,4])


def checkIfSortedAndRotated(nums):
    count_breaks = 0
    n = len(nums)

    # Traverse the array and count breaks in the sorted order (no wrap-around)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            count_breaks += 1

    # Now check the wrap-around case: last element to the first
    if nums[n - 1] > nums[0]:
        count_breaks += 1

    # If there is more than one break, it's not a valid rotated sorted array
    return count_breaks <= 1

# Example usage:
nums = [3, 4, 5, 1, 2]
print(checkIfSortedAndRotated(nums))  # Output: True
    