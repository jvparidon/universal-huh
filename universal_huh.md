
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
    display_md(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').rename_axis('idx').head(10).to_markdown())
    display_md('---')
```


### ABA sequence B-word frequencies for language: af



|   idx | word   |   count |
|------:|:-------|--------:|
|     0 | wat    |       4 |



---



### ABA sequence B-word frequencies for language: fi



|   idx | word       |   count |
|------:|:-----------|--------:|
|     0 | mitä       |    1847 |
|     1 | anteeksi   |     154 |
|     2 | mikä       |     135 |
|     3 | haloo      |     127 |
|     4 | kuka       |      70 |
|     5 | miksi      |      69 |
|     6 | niinkö     |      67 |
|     7 | niin       |      64 |
|     8 | kuuletko   |      62 |
|     9 | kuuletteko |      56 |



---



### ABA sequence B-word frequencies for language: nl



|   idx | word   |   count |
|------:|:-------|--------:|
|     0 | wat    |    3058 |
|     1 | pardon |     385 |
|     2 | hallo  |     275 |
|     3 | ja     |     186 |
|     4 | wie    |     175 |
|     5 | echt   |     147 |
|     6 | nee    |     144 |
|     7 | sorry  |     124 |
|     8 | waarom |     115 |
|     9 | jij    |      96 |



---



### ABA sequence B-word frequencies for language: tr



|   idx | word      |   count |
|------:|:----------|--------:|
|     0 | ne        |    7187 |
|     1 | efendim   |     559 |
|     2 | neredesin |     409 |
|     3 | neden     |     333 |
|     4 | pardon    |     325 |
|     5 | kim       |     287 |
|     6 | alo       |     276 |
|     7 | merhaba   |     270 |
|     8 | evet      |     268 |
|     9 | nerede    |     260 |



---


In every language tested here, the highest frequency B-word is the equivalent of "what" (i.e., "wat", "mitä", and "ne" all mean "what").  
Asking "what?" is not an unreasonable way to initiate a repair, but of course we were looking for "huh" equivalents.  
We can try our procedure on English, to see what kind of results we get for the language the majority of subtitles are translated from.


```python
lang = 'en'
display_md(f'### ABA sequence B-word frequencies for language: {lang}')
display_md(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').rename_axis('idx').head(10).to_markdown())
display_md('---')
```


### ABA sequence B-word frequencies for language: en



|   idx | word   |   count |
|------:|:-------|--------:|
|     0 | what   |   18991 |
|     1 | nan    |    4145 |
|     2 | huh    |    3229 |
|     3 | hello  |    2167 |
|     4 | really |    1548 |
|     5 | why    |    1461 |
|     6 | yeah   |    1389 |
|     7 | no     |    1058 |
|     8 | who    |     990 |
|     9 | okay   |     984 |



---


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
    display_md(pd.read_csv(f'embedding_method/en-{lang}_muse_neighbors.tsv', sep='\t').rename_axis('idx').head(10).to_markdown())
    display_md('---')
```


### Cross-linguistic cosine distances for language: af



|   idx | word        |   cosine_distance |
|------:|:------------|------------------:|
|     0 | Hê          |          0.2196   |
|     1 | liefie      |          0.237689 |
|     2 | nê          |          0.238153 |
|     3 | Pappatjie   |          0.240027 |
|     4 | slivovitz   |          0.244561 |
|     5 | my_liefling |          0.247401 |
|     6 | Mammie      |          0.24974  |
|     7 | nè          |          0.252405 |
|     8 | jou         |          0.255947 |
|     9 | my          |          0.256397 |



---



### Cross-linguistic cosine distances for language: fi



|   idx | word        |   cosine_distance |
|------:|:------------|------------------:|
|     0 | poju        |          0.214634 |
|     1 | kamu        |          0.223444 |
|     2 | häh         |          0.225935 |
|     3 | ystäväiseni |          0.227547 |
|     4 | kultsi      |          0.233309 |
|     5 | pikkukaveri |          0.23373  |
|     6 | helkkari    |          0.234174 |
|     7 | pikkumies   |          0.235422 |
|     8 | helkkarin   |          0.235567 |
|     9 | herraseni   |          0.239839 |



---



### Cross-linguistic cosine distances for language: nl



|   idx | word      |   cosine_distance |
|------:|:----------|------------------:|
|     0 | huh       |          0.159184 |
|     1 | schatje   |          0.162617 |
|     2 | lieverd   |          0.174831 |
|     3 | liefje    |          0.178294 |
|     4 | hé        |          0.180575 |
|     5 | hè        |          0.181786 |
|     6 | makker    |          0.187827 |
|     7 | meneertje |          0.194914 |
|     8 | mam       |          0.202271 |
|     9 | oké       |          0.202835 |



---



### Cross-linguistic cosine distances for language: tr



|   idx | word       |   cosine_distance |
|------:|:-----------|------------------:|
|     0 | dostum     |          0.217794 |
|     1 | </s>       |          0.226429 |
|     2 | ha         |          0.231013 |
|     3 | ahbap      |          0.23277  |
|     4 | huh        |          0.237431 |
|     5 | adamım     |          0.239443 |
|     6 | koca_oğlan |          0.242911 |
|     7 | tatlım     |          0.247647 |
|     8 | Hey        |          0.250283 |
|     9 | beyler     |          0.253327 |



---


These results are a lot closer than the dialogue method results. For Afrikaans and Dutch we get the correct answer in first place, for Turkish and Finnish the correct answer is in third place.  
Because this method is based on distances between language pairs, there is no set of English results (the cosine distance would be zero).

Note that many of the lower-ranked but still close neighbors appear to be in a distinct semantic category: words equivalent to "honey", "buddy", "mommy" and the like. Maybe we can call this category 'terms of endearment'?  
It's worth pondering why these words, in particular, seem close to huh. My hypothesis is that they occur in a similar context to "huh" in that they are used in a wide variety of contexts, but often either in isolation or at the end of sentences, just like "huh".

## Combining evidence from both methods
Neither of the methods used above is perfect, but since they provide evidence from different angles, we can combine the rankings they provide to come to a better answer. We simply sum the rankings of the top 100 answers generated by each method and look for the lowest summed rank.


```python
for lang in langs:
    if lang != 'af':
        display_md(f'### Combined rankings for language: {lang}')
        display_md(pd.read_csv(f'{lang}_ranks.tsv', sep='\t').head(10).rename_axis('idx').head(10).to_markdown())
        display_md('---')
```


### Combined rankings for language: fi



|   idx | word      |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:----------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | häh       |      17 |          0.225935 |       24 |        2 |         26 |
|     1 | nyt       |       7 |          0.247161 |       75 |       18 |         93 |
|     2 | kultaseni |       5 |          0.245345 |       96 |       13 |        109 |



---



### Combined rankings for language: nl



|   idx | word    |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:--------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | huh     |      51 |          0.159184 |       15 |        0 |         15 |
|     1 | oké     |      88 |          0.202835 |       11 |        9 |         20 |
|     2 | mam     |      37 |          0.202271 |       19 |        8 |         27 |
|     3 | papa    |      41 |          0.218817 |       17 |       19 |         36 |
|     4 | pap     |      30 |          0.211262 |       26 |       13 |         39 |
|     5 | hè      |      21 |          0.181786 |       39 |        5 |         44 |
|     6 | schatje |      13 |          0.162617 |       58 |        1 |         59 |
|     7 | hé      |      13 |          0.180575 |       63 |        4 |         67 |
|     8 | lieverd |      10 |          0.174831 |       93 |        2 |         95 |
|     9 | eh      |       7 |          0.213423 |      136 |       15 |        151 |



---



### Combined rankings for language: tr



|   idx | word    |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:--------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | ha      |     233 |          0.231013 |       11 |        2 |         13 |
|     1 | tatlım  |      78 |          0.247647 |       20 |        7 |         27 |
|     2 | huh     |      49 |          0.237431 |       27 |        4 |         31 |
|     3 | bebeğim |      15 |          0.255516 |      104 |       11 |        115 |
|     4 | ahbap   |       5 |          0.23277  |      459 |        3 |        462 |
|     5 | kanka   |       3 |          0.262215 |      727 |       13 |        740 |
|     6 | dostum  |       2 |          0.217794 |     1259 |        0 |       1259 |



---


As we can see, this method yields the correct answer in each language. (We exclude Afrikaans, because the only hit in Afrikaans using the dialogue method was "wat" and that word isn't present in the top 100 of cross-linguistic nearest neighbors for Afrikaans.)
