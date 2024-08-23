#max ascii value of character in a string

string='zhello'

for ch in string:
    ascii_val=ord(ch)
    min_val=0
    if(ascii_val>min_val):
        min_val=ascii_val
    
print(chr(min_val))
    