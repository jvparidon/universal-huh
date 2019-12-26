import numpy as np
import argparse
import subs2vec.vecs
import scipy.spatial.distance


# cosine similarity (assumes vectors are normalized to unit length)
def cos_pos(a, b):
    return (1.0 + np.matmul(a, b.T)) / 2.0


def crosslinguistic_nn(word, source_lang, target_lang):
    source_fname = f'{source_lang}.vec'
    target_fname = f'{target_lang}.vec'
    vecs_source = subs2vec.vecs.Vectors(source_fname)
    vecs_target = subs2vec.vecs.Vectors(target_fname)

    dist = scipy.spatial.distance.cosine(vecs_source.vectors[vecs_source.words == word], vecs_target.vectors)
    sort_idx = np.argsort(dist, axis=0)
    neighbors = vecs_target.words[sort_idx]
    return neighbors


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('word')
    argparser.add_argument('source_lang')
    argparser.add_argument('target_lang')
    args = argparser.parse_args()

    neighbors = crosslinguistic_nn(**vars(args))
    print(neighbors[0:25])
