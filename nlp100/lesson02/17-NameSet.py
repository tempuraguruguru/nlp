if __name__ == '__main__':
    lines = []
    with open('./data/popular-names.txt', 'r') as file:
        for line in file:
            lines.append(line.split(' ')[0])
    set = sorted(set(lines))
    print(set)

# cut -d ' ' -f 1 "[PATH]/popular-names.txt"|sort|uniq