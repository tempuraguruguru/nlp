import random

# 単語で分割
def N_gram_word(n, text):
    res = []
    words = text.split(" ")
    for i in range(len(words)-(n-1)):
        line = ""
        for w in range(n):
            line += words[i] + " "
        res.append(line.rstrip(" "))
    return res

if __name__ == '__main__':
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    dict = {} # keyは単語の順番、valueは配置する単語
    words = N_gram_word(1, text)
    rwords = [] # ランダムに配置する単語
    for i in range(len(words)):
        if i == 0 or i == len(words)-1 or len(words[i]) <= 4:
            dict[i] = words[i]
        else:
            dict[i] = ""
            rwords.append(words[i])
    random.shuffle(rwords)
    for key, value in dict.items():
        if value == "":
            dict[key] = rwords.pop()
    res = ""
    for key, value in dict.items():
        res += value + " "
    print(res.rstrip(" "))