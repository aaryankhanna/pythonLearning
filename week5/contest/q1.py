# join words with space between them of list without using join

def concat(lst):
    result = ""
    for i in lst:
        result = result + i+" "
    print(result)


lst = ['hello', 'world', 'python']
concat(lst)
