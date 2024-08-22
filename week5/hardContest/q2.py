# return a string with max frequrncy char at start

def maxFreq(string):
    freq_dict = dict()
    for i in range(len(string)):
        freq_dict[string[i]] = freq_dict.get(string[i], 0)+1

    result = ""
    check = sorted(freq_dict, key=lambda x: freq_dict[x], reverse=True)

    for i in check:
        num = freq_dict[i]
        result += i*num
    print(result)


string = "heelllllooo"
maxFreq(string)
