import argparse
import pandas as pd


def sum_ranks(lang):
    e_ranks = pd.read_csv(f'embedding_method/en-{lang}_muse_neighbors.tsv', sep='\t')
    d_ranks = pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t')
    e_ranks['e_rank'] = list(range(len(e_ranks)))
    d_ranks['d_rank'] = list(range(len(d_ranks)))
    ranks = e_ranks.merge(d_ranks, how='inner', on='word')
    ranks['sum_rank'] = ranks['e_rank'] + ranks['d_rank']
    combined_ranks = ranks.sort_values('sum_rank').head(10)[['word', 'count', 'cosine_distance', 'd_rank', 'e_rank', 'sum_rank']]
    return combined_ranks


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    args = argparser.parse_args()

    df = sum_ranks(args.lang)
    print(df.head(10))
    df.head(100).to_csv(f'{args.lang}_ranks.tsv', sep='\t', index=False)
