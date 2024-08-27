#pallindrome string using recursion

def palind(s):
    cleaned_string = ''.join(char for char in s if char.isalnum())
    print(len(cleaned_string))
    check=checkPal(cleaned_string.lower(),0,len(cleaned_string)-1)
    print(check)
      
def checkPal(string,start,end):
    if start >= end:
        return True
    elif string[start]==string[end]:
        return checkPal(string,start+1,end-1)
    else:
        return False
        

s = "A man, a plan, a canal: Panama"
palind(s)
