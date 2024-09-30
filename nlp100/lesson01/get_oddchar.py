def odd_char(str):
    res = ""
    for i in range(0, len(str), 2):
        res += str[i]
    return res

if __name__ == '__main__':
    print(odd_char("123456789"))