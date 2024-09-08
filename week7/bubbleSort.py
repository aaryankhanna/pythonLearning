#Bubble Sort - Swap adjacent elements such that largest goes to the last

def bubbleSort(arr):   
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
    
arr = [4, 1, 3, 9, 7]
bubbleSort(arr)