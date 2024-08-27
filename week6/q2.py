# list of all factorial numbers till n
def factNumbers(n):
    result=[]
    ans=1
    for i in range(1,n+1):
        ans=fact(i)
        if ans<=n:
            result.append(ans)
        else:
            return result
        
    
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=6
print(factNumbers(n))