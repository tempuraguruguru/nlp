def TabsToSpace(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.replace("	", " "))
    with open(path, 'w') as file:
        for line in lines:
            file.write(f'{line}')

if __name__ == '__main__':
    # sed -e 's/\t/ /g' ./././nlp100/lesson02/data/popular-names.txt
    TabsToSpace('./././nlp100/lesson02/data/popular-names.txt')

# cat '[PATH]/popular-names.txt' | sed 's/\t/ /'
# cat '[PATH]/popular-names.txt' | tr '\t' ' '
# cat '[PATH]/popular-names.txt' | expand