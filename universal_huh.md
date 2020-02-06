---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Finding cross-linguistic analogues to "huh"

```python
import pandas as pd
from IPython.display import display, display_markdown

def display_md(md, **kwargs):
    return display_markdown(md, raw=True, **kwargs)

langs = ['af', 'fi', 'nl', 'tr']  # these are the languages we will be examining in this pilot
```

## Repair initiation in dialogue method
To find repair initiation in our subtitle corpus, we use the following sequence of steps:

1. Parse subtitle files and extract the text and timestamp for each utterance
2. Find all ABA sequences, meaning an utterance A, followed by an utterance B, followed by the identical utterance A
3. Reject B if it is identical to A (making it an AAA sequence)
4. Reject B if it is more than one word
5. Reject B if it is not a question (does not end in "?")
6. Count frequencies of B

These Bs are potential repair initiations; they are one-word questions that provoke a repetition of the preceding utterance. A possible weakness in this method is that straight repeats aren't necessarily very good repairs, but it is very difficult to define a usable rule to search for sequences that would constitute good repairs.

```python
for lang in langs:
    display_md(f'### ABA sequence B-word frequencies for language: {lang}')
    display(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').head(10))
    display_md('---')
```

In every language tested here, the highest frequency B-word is the equivalent of "what" (i.e., "wat", "mitä", and "ne" all mean "what").  
Asking "what?" is not an unreasonable way to initiate a repair, but of course we were looking for "huh" equivalents.  
We can try our procedure on English, to see what kind of results we get for the language the majority of subtitles are translated from.

```python
lang = 'en'
display_md(f'### ABA sequence B-word frequencies for language: {lang}')
print(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').head().to_markdown())
display_md('---')
```

Even in English "what" is the most frequent B-word, by far.  
However, for English "huh" is the third item, much more frequent than in other languages. Two factors might partially explain why "what" is more prevalent than "huh" in English and even more so in other languages.

1. Scriptwriters prefer to use a more lexicalized repair initiation, whereas in real life people are likely to use "huh?" and its equivalents.
2. That same cognitive bias toward lexicalized repair initiations affects translators. As dialogue is transcribed and translated, "huh" sometimes gets turned into "what", for instance. This results in a further decrease in the fraction of "huh" equivalents.

(It's worth noting that the second entry, "NaN" is actually just a solitary question mark ("?") instead of an actual word. It's unclear what these question marks represent. It could be any kind of communicative act, possibly including utterances like "huh".)  


## Cross-linguistic nearest neighbor method
This method makes use of word embeddings, vector representations of words, to find cross-linguistic equivalents of "huh".

1. Train word embeddings on subtitles (and Wikipedia, to increase the size of the training corpus) in every available language
2. Align embeddings in different languages to the English embeddings (by iteratively shrinking the cosine distance between dictionary-derived word translation pairs)
3. Find cross-linguistic nearest neighbor of "huh" in every English/other language pair using cosine distances

Word embedding vectors are a numerical representation of the typical context a word is found in. Given that equivalents of "huh" are likely to occur in similar contexts to "huh", we expect the word vectors (in aligned spaces) to be highly similar, reflected in a small cosine distance.

```python
for lang in langs:
    display_md(f'### Cross-linguistic cosine distances for language: {lang}')
    display(pd.read_csv(f'embedding_method/en-{lang}_muse_neighbors.tsv', sep='\t').head(10))
    display_md('---')
```

These results are a lot closer than the dialogue method results. For Afrikaans and Dutch we get the correct answer in first place, for Turkish and Finnish the correct answer is in third place.  
Because this method is based on distances between language pairs, there is no set of English results (the cosine distance would be zero).

Note that many of the lower-ranked but still close neighbors appear to be in a distinct semantic category: words equivalent to "honey", "buddy", "mommy" and the like. Maybe we can call this category 'terms of endearment'?  
It's worth pondering why these words, in particular, seem close to huh. My hypothesis is that they occur in a similar context to "huh" in that they are used in a wide variety of contexts, but often either in isolation or at the end of sentences, just like "huh".


## Combining evidence from both methods
Neither of the methods used above is perfect, but since they provide evidence from different angles, we can combine the rankings they provide to come to a better answer. We simply sum the rankings of the top 100 answers generated by each method and look for the lowest summed rank.

```python
for lang in langs:
    display_md(f'### Combined rankings for language: {lang}')
    display(pd.read_csv(f'{lang}_ranks.tsv', sep='\t').head(10))
    display_md('---')
```

As we can see, this method yields the correct answer in every language but Afrikaans, because the only hit in Afrikaans using the dialogue method was "wat" and that word isn't present in the top 100 of cross-linguistic nearest neighbors for Afrikaans.
