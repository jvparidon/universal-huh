import argparse


def parse_line(line):
    line = line.split(']')
    try:
        timestamp = float(line[0].split('[')[1].replace(' ', '').replace('-', ''))
    except ValueError:
        timestamp = 0
    stripped = line[1]
    return stripped, timestamp


def strip_line(line):
    return line.replace('-', '').strip(' ').lower()


def is_question(line):
    """Takes a line and checks if it is a question.

    This function tries to take into account different methods of marking a question in various languages,
    but is very unlikely to be exhaustive.

    :param line: line to check
    :return: boolean, True if line is a question, else False
    """
    if line.startswith('؟') or line.startswith('⸮'):  # arabic question mark, should appear at beginning of line (because arabic is right-to-left)
        return True
    elif line.endswith('?'):  # latin question mark
        return True
    elif line.startswith('?'):  # hebrew question mark, should appear at beginning of line (because hebrew is right-to-left)
        return True
    elif line.endswith(';') or line.endswith(';'):  # greek question mark
        return True
    elif line.endswith('՞'):  # armenian question mark
        return True
    else:
        return False  # not a question, it would seem


def find_b(lang, fname=None, verbose=True):
    if fname is None:
        fname = f'{lang}_aba.txt'
    with open(fname, 'r') as abafile, open(f'{lang}_b.txt', 'w') as bfile:
        abatext = abafile.read().split('\n')  # read text and split into list of lines
        for i, line in enumerate(abatext):  # iterate over lines, but keep track of index
            if line.startswith('B'):  # check if a line is a B line (in ABA sequence)
                parsed_b, time_b = parse_line(line)  # parse B line into utterance and timestamp
                parsed_a, time_a1 = parse_line(abatext[i - 1])  # parse A1 line into utterance and timestamp
                parsed_a, time_a2 = parse_line(abatext[i + 1])  # parse A2 line into utterance and timestamp
                if parsed_b.startswith('  ') ^ parsed_a.startswith('  '):
                    stripped_a = strip_line(parsed_a)
                    stripped_b = strip_line(parsed_b)
                    if stripped_b != stripped_a:  # check if B line is not identical to A lines
                        if (len(stripped_b.split(' ')) == 1) and is_question(stripped_b):  # check if line is one word and is a question
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
