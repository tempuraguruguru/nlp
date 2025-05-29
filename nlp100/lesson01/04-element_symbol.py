def str_split(text):
    text = text.replace(",", "").replace(".", "")
    words = text.split(" ")
    return words

def str_cutout(str, length):
    return str[0:length]

if __name__ == '__main__':
    str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = str_split(str)
    index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    dict = {}
    for i in range(len(words)):
        if i+1 in index:
            word = str_cutout(words[i], 1)
        else:
            word = str_cutout(words[i], 2)
        dict[word] = i+1
    print(dict)