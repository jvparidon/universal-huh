import numpy as np
import pandas as pd
import argparse
import subs2vec.vecs


def crosslinguistic_nn(word, source_lang, target_lang):

    # cosine similarity (assumes vectors are normalized to unit length)
    def cos_dist(a, b):
        return (1.0 - np.matmul(a, b.T)) / 2.0

    source_fname = f'{source_lang}.aligned.vec'
    target_fname = f'{target_lang}.aligned.vec'
    #source_fname = f'wiki.multi.{source_lang}.vec'
    #target_fname = f'wiki.multi.{target_lang}.vec'
    vecs_source = subs2vec.vecs.Vectors(source_fname, normalize=True, n=1e5)
    vecs_target = subs2vec.vecs.Vectors(target_fname, normalize=True, n=1e5)
    dist = cos_dist(vecs_source.vectors[vecs_source.words == word], vecs_target.vectors)
    sort_idx = np.argsort(dist, axis=1)
    neighbors = vecs_target.words[sort_idx]
    df = pd.DataFrame(np.hstack([neighbors.T, dist[0, sort_idx].T]), columns=['neighbors', 'cosine_dists'])
    return df


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('word')
    argparser.add_argument('source_lang')
    argparser.add_argument('target_lang')
    args = argparser.parse_args()

    df = crosslinguistic_nn(**vars(args))
    print(df.head(10))
    df.to_csv('neighbors.tsv', sep='\t', index=False)
