def N_gram_char(n, text):
    res = []
    for i in range(len(text)-(n-1)):
        res.append(text[i:i+n])
    return res

if __name__ == '__main__':
    X = set(N_gram_char(2, "paraparaparadise"))
    Y = set(N_gram_char(2, "paragraph"))
    print(f"X = {X}")
    print(f"Y = {Y}")
    print(f"X | Y = {X | Y}") # 和集合
    print(f"X & Y = {X & Y}") # 積集合
    print(f"X - Y = {X - Y}") # 差集合
    if "se" in X:
        print(f"X have 'se'")
    if "se" in Y:
        print(f"Y have 'se'")