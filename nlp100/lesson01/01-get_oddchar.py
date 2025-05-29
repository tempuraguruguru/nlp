def odd_char(str):
    res = ""
    for i in range(0, len(str), 2):
        res += str[i]
    return res

def even_char(str):
    res = ""
    for i in range(1, len(str), 2):
        res += str[i]
    return res

if __name__ == '__main__':
    text = "パタトクカシーー"
    print(even_char(text))
    print(odd_char(text))