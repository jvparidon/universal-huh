import numpy as np
import pandas as pd
import argparse
import subs2vec.vecs
# TODO fix source/target language terminology? (semantically confusing)


# from https://stackoverflow.com/questions/21030391/how-to-normalize-array-numpy
def normalized(a, axis=-1, order=2):
    """Utility function to normalize the rows of a numpy array."""
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)


# CODE FROM: https://github.com/Babylonpartners/fastText_multilingual
def make_training_matrices(source_dictionary, target_dictionary, bilingual_dictionary):
    """
    Source and target dictionaries are the FastVector objects of
    source/target languages. bilingual_dictionary is a list of
    translation pair tuples [(source_word, target_word), ...].
    """
    source_matrix = []
    target_matrix = []
    for (source, target) in bilingual_dictionary:
        if source in source_dictionary and target in target_dictionary:
            source_matrix.append(source_dictionary[source])
            target_matrix.append(target_dictionary[target])
    # return training matrices
    print(len(source_matrix))
    return np.array(source_matrix), np.array(target_matrix)


# CODE FROM: https://github.com/Babylonpartners/fastText_multilingual
def learn_transformation(source_matrix, target_matrix, normalize_vectors=False):
    """
    Source and target matrices are numpy arrays, shape
    (dictionary_length, embedding_dimension). These contain paired
    word vectors from the bilingual dictionary.
    """
    # optionally normalize the training vectors
    if normalize_vectors:
        source_matrix = normalized(source_matrix)
        target_matrix = normalized(target_matrix)
    # perform the SVD
    product = np.matmul(source_matrix.T, target_matrix)
    U, s, V = np.linalg.svd(product)
    # return orthogonal transformation which aligns source language to the target
    return np.matmul(U, V)


def realign_embeddings(lang, align_to):

    # load dictionary
    df = pd.read_csv(f'dictionaries/{align_to}-{lang}.csv')
    print(len(df))
    lang_words = list(df[lang])
    align_to_words = list(df[align_to])
    bilingual_dictionary = list(zip(align_to_words, lang_words))

    # load source and target vectors
    source_vecs = subs2vec.vecs.Vectors(f'../../for_publication/{align_to}/wiki-subs.{align_to}.1e6.vec', normalize=True, n=1e5)
    source_vecs_dict = source_vecs.as_dict()
    target_vecs = subs2vec.vecs.Vectors(f'../../for_publication/{lang}/wiki-subs.{lang}.1e6.vec', normalize=True, n=1e5)
    target_vecs_dict = target_vecs.as_dict()
    source_dictionary = {word: source_vecs_dict.get(word, None) for word in align_to_words if source_vecs_dict.get(word, None) is not None}
    target_dictionary = {word: target_vecs_dict.get(word, None) for word in lang_words if target_vecs_dict.get(word, None) is not None}

    '''
    for word, vec in source_dictionary.items():
        if vec is None:
            del source_dictionary[word]
    for word, vec in target_dictionary.items():
        if vec is None:
            del target_dictionary[word]
    '''

    # learn mapping
    source_matrix, target_matrix = make_training_matrices(source_dictionary, target_dictionary, bilingual_dictionary)
    transform = learn_transformation(source_matrix, target_matrix)
    print('transform matrix shape')
    print(transform.shape)
    # apply mapping
    target_vecs.vectors = np.matmul(target_vecs.vectors, transform)
    print('transformed vecs shape')
    print(target_vecs.vectors.shape)

    # write aligned vectors to file
    target_vecs.write_vecs(f'{lang}.aligned.vec')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('align_to')
    args = argparser.parse_args()

    realign_embeddings(**vars(args))
