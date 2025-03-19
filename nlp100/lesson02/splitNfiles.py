import numpy as np
import os

def SplitNfiles(path, n):
    with open(path, 'r') as file:
        lines = file.readlines()
    row_count = len(lines)
    num_list = range(row_count)
    split_list = np.array_split(num_list, n)
    for i, split in enumerate(split_list, 1):
        file = open(f'./output/{str(i).zfill(3)}.txt', 'w')
        for j in split:
            file.write(lines[j])
        file.close()


if __name__ == '__main__':
    input_path = './data/popular-names.txt'
    SplitNfiles(input_path, 10)

# split -n 3 -d --additional-suffix=.txt "[PATH]/popular-names.txt" "[出力先のPATH]"