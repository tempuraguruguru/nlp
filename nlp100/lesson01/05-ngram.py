def N_gram_char(n, text):
    res = []
    for i in range(len(text)-(n-1)):
        res.append(text[i:i+n])
    return res

def N_gram_word(n, text):
    res = []
    words = text.split(" ")
    for i in range(len(words)-(n-1)):
        res.append(f"{words[i]} {words[i+1]}")
    return res

if __name__ == '__main__':
    text = "I am an NLPer"
    print(N_gram_char(3, text))
    print(N_gram_word(2, text))