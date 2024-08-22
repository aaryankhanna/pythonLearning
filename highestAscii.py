# find highest ascii value character in a string
string="aryan"

j=1
max=ord(string[0])
while j<len(string):
    if ord(string[j])>max:
        max=ord(string[j])
    j+=1


max_chr=chr(max)
print(max_chr)
