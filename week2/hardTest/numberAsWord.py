# print number to word
   
def lastDigit(result):
    match lst[-1]:
        case 1 : result += "one"
        case 2 : result +="Two"
        case 3 : result +="Three"
        case 4 : result +="Four"
        case 5 : result +="Five"
        case 6 : result +="Six"
        case 7 : result +="Seven"
        case 8 : result +="Eight"
        case 9 : result +="Nine" 
    return result

def convertingToList(num): 
    lst=[]
    rem=0
    while(num>=1):
        rem=num%10
        num=num//10
        lst.append(rem)
    lst=lst[::-1]  
    return lst

def secondLastDigit(result,num):
    match num:
        case 2 : result +="Twenty"
        case 3 : result +="Thirty"
        case 4 : result +="Fourty"
        case 5 : result +="Fifty"
        case 6 : result +="Sixty"
        case 7 : result +="Seventy"
        case 8 : result +="Eighty"
        case 9 : result +="Ninty"
    return lastDigit(result)
    


def secondLastOne(result , num):
    match num:
        case 0 : result+= "Ten"
        case 1 : result += "Eleven"
        case 2 : result +="Tweleve"
        case 3 : result +="Thirteen"
        case 4 : result +="Fourteen"
        case 5 : result +="Fifteen"
        case 6 : result +="Sixteen"
        case 7 : result +="Seventeen"
        case 8 : result +="Eighteen"
        case 9 : result +="Nineteen" 
    return result




n=45
lst=[]
result=""
if n == 0:
     print("Zero") 
else:
    lst=convertingToList(n)
    if len(lst)>1:
        if lst[-2] != 1:
            result=secondLastDigit(result,lst[-2])
        else:
            result=secondLastOne(result,lst[-1])
    else:
        result=lastDigit(result)
    print(result)


