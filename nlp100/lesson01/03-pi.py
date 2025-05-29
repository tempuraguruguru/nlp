def splitANDnum_word(str):
    res = []
    str = ((str.replace(",", "")).replace(".", ""))
    words = str.split(" ")
    for word in words:
        res.append(len(word))
    return res

if __name__ == '__main__':
    print(splitANDnum_word("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))