#Frequencies of Limited Range Array Elements Hashing

def freq(n,arr,p):
    l=[0]*n
    print(l)
    for i in range(1,n+1):
        if i <=p:
            l[i]+=1
    print(l)    
            
        
    



n = 5
arr = [2, 3, 2, 3, 5]
p = 5
freq(n,arr,p)