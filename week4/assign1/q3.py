l1=[1,2,3,4]
l2=[5,6,7,1]
flag = False
for i in l1:
    if i in l2:
        flag = True
        break
    
print(flag)