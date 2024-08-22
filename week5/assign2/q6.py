# max frequency of a letter in a word

def maxFreq(word):
    freq_dict = dict()
    maxAmount = 0
    alphabet = ""
    for i in range(len(word)):
        freq_dict[word[i]] = freq_dict.get(word[i], 0)+1
    for alpha, freq in freq_dict.items():
        if (freq > maxAmount):
            maxAmount = freq
            alphabet = alpha
    print(alphabet, maxAmount)


word = "hello world"
maxFreq(word)
