l1= [1,2,3,4,5,6,7,8,9]
odd=[]
even=[]
for i in l1:
    even.append(i) if i%2==0 else odd.append(i)


print(f'l1 :',l1)
print(f'odd : ',odd)
print(f'even : ',even)
    