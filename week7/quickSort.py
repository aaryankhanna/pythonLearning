def part(arr,low ,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i <high:
            i=i+1
        while arr[j]>pivot and j>=low:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[j],arr[low]=arr[low],arr[j]
    return j
        
        
    

def quickSort(arr,low,high):
    if low < high:
        index =part(arr,low,high)
        quickSort(arr,low,index-1)
        quickSort(arr,index+1,high)

arr = [5,3,9,2,6,4,7]
quickSort(arr,0,len(arr)-1)
print(arr)
