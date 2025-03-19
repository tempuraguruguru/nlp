def PrintNendLine(path, n):
    lines = []
    with open(path, 'r') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    for i in range(n):
        print(lines[-(i+1)])

if __name__ == '__main__':
    path = input()
    n = int(input())
    PrintNendLine(path, n)

# tail -n 5 "[PATH]/popular-names.txt"