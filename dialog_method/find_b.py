lang = 'en'

with open(f'{lang}_aba.txt', 'r') as abafile, open(f'{lang}_b.txt', 'w') as bfile:
    for line in abafile:
        if line.startswith('B'):
            line = line.split(']')[1]
            line = line.replace('-', '').strip('\n').strip(' ')
            if (len(line.split(' ')) == 1) and line.endswith('?'):
                print(line)
                bfile.write(line + '\n')
