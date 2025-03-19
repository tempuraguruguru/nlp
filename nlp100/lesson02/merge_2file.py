def Merge2File(path1, path2, save_path):
    lines1 = []
    with open(path1, 'r') as file:
        for line in file:
            lines1.append(line.rstrip('\n'))
    lines2 = []
    with open(path2, 'r') as file:
        for line in file:
            lines2.append(line.rstrip('\n'))
    if len(lines1) == len(lines2):
        with open(save_path, 'w') as file:
            for i in range(len(lines1)):
                file.write(f'{lines1[i]}    {lines2[i]}\n')

if __name__ == '__main__':
    Merge2File('./data/col1.txt', './data/col2.txt', './data/merge.txt')

# paste '[PATH]/col1.txt' '[PATH]/col2.txt'