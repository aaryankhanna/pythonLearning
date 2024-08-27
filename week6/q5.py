#The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1.
# return Fibonnaci numbers using recursion


def fibo(n):
    if n<=1 :
        return n
    else:
        return fibo(n-1)+fibo(n-2)
  
n=4
print(fibo(n))