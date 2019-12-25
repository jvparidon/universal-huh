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
    return np.array(source_matrix), np.array(target_matrix)


# CODE FROM: https://github.com/Babylonpartners/fastText_multilingual
def learn_transformation(source_matrix, target_matrix, normalize_vectors=True):
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
    product = np.matmul(source_matrix.transpose(), target_matrix)
    U, s, V = np.linalg.svd(product)
    # return orthogonal transformation which aligns source language to the target
    return np.matmul(U, V)


def realign_embeddings(lang, align_to):

    # load dictionary
    df = pd.read_csv(f'{align_to}-{lang}')
    bilingual_dictionary = [(row[align_to], row[lang]) for row in df.iterrows()]

    # load source and target vectors


    # prep dictionaries
    source_dictionary = dict(zip(source_language_vocabulary, source_language_vectors))
    target_dictionary = dict(zip(target_language_vocabulary, target_language_vectors))

    # learn mapping
    source_matrix, target_matrix = make_training_matrices(source_dictionary, target_dictionary, bilingual_dictionary)
    transform = learn_transformation(source_matrix, target_matrix)

    # apply mapping
    aligned_target_vectors = np.matmul(target_vectors, transform)

    # write aligned vectors to file


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('lang')
    argparser.add_argument('align_to')
    args = argparser.parse_args()

    realign_embeddings(vars(args))
