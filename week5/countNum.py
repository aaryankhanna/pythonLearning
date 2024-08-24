# count the number of times a number appear in a list using dictionary

def countNum(lst):
    n=len(lst)
    freq_dict=dict()
    for i in range(n):
        freq_dict[lst[i]]=freq_dict.get(lst[i],0)+1
    return freq_dict
    
    
    
    
lst=[1,2,3,4,1,1,1,6,7,2,3,3]
print(countNum(lst))