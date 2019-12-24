import collections
import argparse
import pandas as pd


def find_freqs(lang, fname=None):
    if fname is None:
        fname = f'{lang}_b.txt'
    with open(fname, 'r') as bfile:
        txt = bfile.read()
        words = txt.split('\n')
        freqs = collections.Counter(words)
        df = pd.DataFrame(freqs.most_common(), columns=['word', 'count'])
        df.to_csv(f'{lang}_freqs.tsv', sep='\t', index=False)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        find_freqs(lang=args.lang, fname=args.fname)
    else:
        find_freqs(lang=args.lang)
