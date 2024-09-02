#Insertion Sort

def insertionSort(arr):
    for i in range(1,len(arr)):
        print('i: ',i)
        for j in range(i,0,-1):
            print("j : ",j)
            print("arr[j] : ",arr[j] , "arr[i] : ",arr[i])
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
            print(arr)
            
    print(arr)

arr=[23, 1, 10, 5, 2]
insertionSort(arr)