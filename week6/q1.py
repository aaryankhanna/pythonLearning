# sum of cube of n terms using recursion
def cubeSum(n):
    if n>0:
        return cubeSum(n-1)+n**3
    else:
        return 0
n=5
print(cubeSum(n))