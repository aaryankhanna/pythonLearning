# print N to 1 using Recursion
def printNto1(n):
    if n<=0:
        return
    print(n)
    printNto1(n-1)


n =5
printNto1(n)