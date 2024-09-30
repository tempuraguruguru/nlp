def cipher(text):
    res = ""
    for char in text:
        if not char.isupper():
            res += f"219-{ord(char)}"
        else:
            res += char
    return res

if __name__ == '__main__':
    text = "I am a NLPer"
    print(cipher(text))