import argparse


def find_aba(lang, fname=None):
    if fname is None:
        fname = f'../data/OpenSubtitles/raw/{lang}/{lang}.txt'
    with open(fname, 'r') as subsfile, open(f'{lang}_repairs.txt', 'w') as abafile:
        line1back = ''
        line2back = ''
        for line in subsfile:
            if line.strip('\n').strip('\t').strip(' ') != '':
                if line == line2back:
                    aba = f'A\t{line2back}B\t{line1back}A\t{line}\n'
                    print(aba)
                    abafile.write(aba)
                line2back = line1back
                line1back = line


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        find_aba(lang=args.lang, fname=args.fname)
    else:
        find_aba(lang=args.lang)
