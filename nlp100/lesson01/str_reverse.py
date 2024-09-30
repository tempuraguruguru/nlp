def reverse(str):
    res = ""
    for c in str:
        res = c + res
    return res

if __name__ == '__main__':
    print(reverse("stressed"))