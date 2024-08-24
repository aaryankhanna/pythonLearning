#remove duplicates from list and print it

l1=[1,2,1,3,4,5,6,1,2,3,1]
l2=[]
l1.sort()
print(l1)
i=0
j=1
while(j<len(l1)):
    if(l1[i]==l1[j]):
        if l1[i] not in l2:
            l2.append(l1[j])
        l1.remove(l1[j])
    else:
        if l1[i] in l2:
            l1.remove(l1[i])
        else:
            i+=1
        j=i+1
          
print(f'l1',l1)
print(f'l2',l2)
