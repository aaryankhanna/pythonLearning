# Frequencies of Limited Range Array Elements Hashing

def freq(n, arr, p):
    l = [0]*(n)

    print(l)
    if p < n:
        for i in range(len(arr)):
            l[arr[i]-1] += 1
        print(l)
    else:
        print(l)


n = 10
arr = [8, 9]
p = 5
freq(n, arr, p)
