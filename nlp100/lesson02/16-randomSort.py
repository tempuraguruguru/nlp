import random

def sort_random(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line)
    random.shuffle(lines)
    with open(path, 'w') as file:
        for line in lines:
            file.write(line)

if __name__ == '__main__':
    sort_random('./data/popular-names.txt')

