def N_gram_char(n, text):
    res = []
    for i in range(len(text)-(n-1)):
        res.append(text[i:i+n])
    return res

if __name__ == '__main__':
    X = set(N_gram_char(2, "paraparaparadise"))
    Y = set(N_gram_char(2, "paragraph"))
    print(X | Y)
    print(X & Y)
    print(X - Y)
    if "se" in X:
        print(f"X have 'se'")
    if "se" in Y:
        print(f"Y have 'se'")