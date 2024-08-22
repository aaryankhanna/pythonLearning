# reverse sub array using recurssion
def reverseArr(arr,l,r):
    print(arr)
    if l>=r:
        return 
    arr[l],arr[r]=arr[r],arr[l]
    reverseArr(arr,l+1,r-1)



arr= [1, 2, 3, 4, 5, 6, 7,8,9,10]  
L = 2 
R = 6
reverseArr(arr,L,R)
print(arr)
