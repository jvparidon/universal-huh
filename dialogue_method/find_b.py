import argparse


def parse_line(line):
    line = line.split(']')
    try:
        timestamp = float(line[0].split('[')[1].replace(' ', '').replace('-', ''))
    except ValueError:
        timestamp = 0
    stripped = line[1].replace('-', '').strip(' ')
    return stripped, timestamp


def find_b(lang, fname=None, verbose=True):
    if fname is None:
        fname = f'{lang}_aba.txt'
    with open(fname, 'r') as abafile, open(f'{lang}_b.txt', 'w') as bfile:
        abatext = abafile.read().split('\n')  # read text and split into list of lines
        for i, line in enumerate(abatext):  # iterate over lines, but keep track of index
            if line.startswith('B'):  # check if a line is a B line (in ABA sequence)
                stripped_b, time_b = parse_line(line)  # parse B line into utterance and timestamp
                stripped_a, time_a1 = parse_line(abatext[i - 1])  # parse A1 line into utterance and timestamp
                stripped_a, time_a2 = parse_line(abatext[i + 1])  # parse A2 line into utterance and timestamp
                if stripped_b != stripped_a:  # check if B line is not identical to A lines
                    if (len(stripped_b.split(' ')) == 1) and stripped_b.endswith('?'):  # check if line is one word and ends in ?
                        bfile.write(stripped_b + '\n')  # write to file

                        if verbose:
                            # some printing for diagnostic purposes
                            print(abatext[i - 1])
                            print(line)
                            print(abatext[i + 1])
                            print('\n')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        find_b(lang=args.lang, fname=args.fname)
    else:
        find_b(lang=args.lang)
