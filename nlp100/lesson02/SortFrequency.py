import pandas as pd

if __name__ == '__main__':
    data = {}
    with open('./data/popular-names.txt', 'r') as file:
        for line in file:
            name = line.rstrip('\n').split(' ')[0]
            if name in data:
                data[name] += 1
            else:
                data[name] = 1
    data = dict(sorted(data.items(), key = lambda x: x[1], reverse = True))
    for k, v in data.items():
        print(f'{k} {v}')

# cut -d ' ' -f 1 "[PATH]/popular-names.txt"|sort|uniq -c|sort -r -n