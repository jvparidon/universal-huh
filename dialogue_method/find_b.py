import argparse


def find_b(lang, fname=None):
    if fname is None:
        fname = f'{lang}_aba.txt'
    with open(fname, 'r') as abafile, open(f'{lang}_b.txt', 'w') as bfile:
        for line in abafile:
            if line.startswith('B'):
                line = line.split(']')[1]
                line = line.replace('-', '').strip('\n').strip(' ')
                if (len(line.split(' ')) == 1) and line.endswith('?'):
                    print(line)
                    bfile.write(line + '\n')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        find_b(lang=args.lang, fname=args.fname)
    else:
        find_b(lang=args.lang)
