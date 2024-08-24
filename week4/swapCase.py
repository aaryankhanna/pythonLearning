string="ASDFGHjsjd123456#(dsndsfdds AnsbdsSADSFGFVC)"
result=str()
for ch in string:
    ascii_code=ord(ch)
    if ascii_code>=65 and ascii_code<=90:
        ascii_code+=32
        result+=chr(ascii_code)
    elif ascii_code>=97 and ascii_code<=122:
        ascii_code-=32
        result+=chr(ascii_code)
    else:
        result+=ch
        
print(result)