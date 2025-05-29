import pandas as pd

if __name__ == '__main__':
    data = {'name': [], 'sex': [], 'people': [], 'age': []}
    with open('./data/popular-names.txt', 'r') as file:
        for line in file:
            lines = line.rstrip('\n').split(' ')
            data['name'].append(lines[0])
            data['sex'].append(lines[1])
            data['people'].append(int(lines[2]))
            data['age'].append(int(lines[3]))
    df = pd.DataFrame(data)
    print(df.sort_values(by = 'people', ascending = False))

# sort -n -r -k 3,3 -t " " "[PATH]/popular-names.txt"