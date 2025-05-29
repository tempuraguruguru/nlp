def merge(s1, s2):
    res = ""
    for c1, c2 in zip(s1, s2):
        res += c1 + c2
    return res

if __name__ == '__main__':
    print(merge("パトカー", "タクシー"))