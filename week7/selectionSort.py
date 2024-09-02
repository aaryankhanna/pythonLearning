#Selection Sort - Swap adjacent elements such that min goes to the first

def selectionSort(arr):   
    for i in range(0,len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)): 
            if arr[j]<arr[minIndex]:
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]
        
    print(arr)
    
arr = [64, 12,11,25, 12, 22, 11]
selectionSort(arr)