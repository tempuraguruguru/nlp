def SaveFile(raw_path, save_row, save_path):
    lines = []
    with open(raw_path, 'r') as file:
        for line in file:
            lines.append(line.split(' ')[save_row])
    with open(save_path, 'w') as file:
        for line in lines:
            file.write(f'{line}\n')

if __name__ == '__main__':
    raw_path = './././nlp100/lesson02/data/popular-names.txt'
    save_path1 = './././nlp100/lesson02/data/col1.txt'
    save_path2 = './././nlp100/lesson02/data/col2.txt'
    SaveFile(raw_path, 0, save_path1)
    SaveFile(raw_path, 1, save_path2)

# 1列目
# cut -f 1 -d " " '[PATH]/popular-names.txt'
# 2列目
# cut -f 2 -d " " '[PATH]/popular-names.txt'