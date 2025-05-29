def cipher(text):
    text_list = []
    words = text.split(" ")
    for word in words:
        word_list = []
        for char in word:
            if not char.isupper():
                word_list.append(f"{219 - int(ord(char))}")
            else:
                word_list.append(char)
        text_list.append(word_list)
    return text_list

def decryption(text):
    res = ""
    for word in text:
        for char in word:
            if char.isupper():
                res += char
            else:
                res += chr(int(char)*-1 + 219)
        res += " "
    return res

if __name__ == '__main__':
    text = "I am a NLPer"
    ord = cipher(text)
    print(ord)
    print(decryption(ord))
