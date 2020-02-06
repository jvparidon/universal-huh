import argparse
import pandas as pd


def combine_ranks(lang):
    e_ranks = pd.read_csv(f'embedding_method/en-{lang}_muse_neighbors.tsv', sep='\t')
    d_ranks = pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t')
    e_ranks['e_rank'] = list(range(len(e_ranks)))
    d_ranks['d_rank'] = list(range(len(d_ranks)))
    ranks = e_ranks.merge(d_ranks, how='inner', left_on='neighbors', right_on='word')
    ranks['rank'] = ranks['e_rank'] + ranks['d_rank']
    combined_ranks = ranks.sort_values('rank').head(10)
    #e_set = set(embedding_ranks['neighbors'].str.lower())
    #d_list = list(dialogue_ranks['word'].str.lower())[0:30]
    #d_set = set([word.strip('?') for word in d_list])
    #combined_ranks = e_set & d_set
    return combined_ranks


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    args = argparser.parse_args()

    print(combine_ranks(args.lang))
