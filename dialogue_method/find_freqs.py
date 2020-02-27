import collections
import argparse
import pandas as pd


def find_freqs(lang, fname=None):
    if fname is None:
        fname = f'{lang}_b.txt'
    with open(fname, 'r') as bfile:
        txt = bfile.read()  # read file
        words = txt.split('\n')  # split into list of words
        freqs = collections.Counter(words)  # count word occurrences
        df = pd.DataFrame(freqs.most_common(), columns=['word', 'count'])  # store counts in pandas df
        df = df[df['count'] > 1]  # remove words with count == 1 (likely to be flukes or misspellings)
        return df


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('--fname')
    args = argparser.parse_args()

    if args.fname:
        df = find_freqs(lang=args.lang, fname=args.fname)
    else:
        df = find_freqs(lang=args.lang)
    
    print(df.head(10))
    df.head(100).to_csv(f'{args.lang}_freqs.tsv', sep='\t', index=False)
