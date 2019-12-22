import collections
import pandas as pd

lang = 'fi'

with open(f'{lang}_b.txt') as bfile:
    txt = bfile.read()
    words = txt.split('\n')
    freqs = collections.Counter(words)
    df = pd.DataFrame(freqs.most_common(), columns=['word', 'count'])
    df.to_csv(f'{lang}_freqs.tsv', sep='\t', index=False)
