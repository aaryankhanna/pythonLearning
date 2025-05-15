def getSecondOrderElements(n, a):
    if n < 2:
        return "Array must have at least two elements"
    
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    
    for num in a:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num

    return [second_largest, second_smallest]

a = [100, 20, 3, 4, 5, 15]
n = len(a)
result = getSecondOrderElements(n, a)
print(result)
