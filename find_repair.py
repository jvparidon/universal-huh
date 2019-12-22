import argparse


def find_repair(lang, fname=None):
    if fname is None:
        fname = f'../data/OpenSubtitles/raw/{lang}/{lang}.txt'
    with open(fname, 'r') as subsfile, open(f'{lang}_repairs.txt', 'w') as repairfile:
        line1back = ''
        line2back = ''
        for line in subsfile:
            if line.strip('\n').strip('\t').strip(' ') != '':
                if line == line2back:
                    # huhfile.write(line1back.replace('\n', '') + '\t' + line)
                    print(line2back + line1back + line + '\n')
                    repairfile.write(line2back + line1back + line + '\n')
                line2back = line1back
                line1back = line


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        find_repair(lang=args.lang, fname=args.fname)
    else:
        find_repair(lang=args.lang)
