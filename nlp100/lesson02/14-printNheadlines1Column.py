def PrintNheadLine1Column(path, n):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    for i in range(n):
        line = lines[i].split(' ')
        print(line[0])

if __name__ == '__main__':
    path = input()
    n = int(input())
    PrintNheadLine1Column(path, n)
