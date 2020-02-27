
# Finding cross-linguistic analogues to "huh"

## To do:
1. Implement whitespace-sensitive method for identifying dialogue ABA (as opposed to monologue ABA)
2. Check if that changes the rankings?
3. Check if Google Translate has an audio API
4. Maybe add 1 non-alphabetic language to the initial (pre-preregistration) dataset?


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
    df = pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').rename_axis('idx')
    if len(df) > 0:
        display_md(df.head(10).to_markdown())
    else:
        display_md(f'No ABA sequences found for language: {lang}')
    display_md('---')
```


### ABA sequence B-word frequencies for language: af



No ABA sequences found for language: af



---



### ABA sequence B-word frequencies for language: fi



|   idx | word      |   count |
|------:|:----------|--------:|
|     0 | mitä?     |    1410 |
|     1 | mikä?     |     120 |
|     2 | anteeksi? |     119 |
|     3 | haloo?    |      81 |
|     4 | kuka?     |      59 |
|     5 | miksi?    |      57 |
|     6 | niinkö?   |      55 |
|     7 | niin?     |      49 |
|     8 | missä?    |      48 |
|     9 | kuuletko? |      48 |



---



### ABA sequence B-word frequencies for language: nl



|   idx | word    |   count |
|------:|:--------|--------:|
|     0 | wat?    |    2043 |
|     1 | pardon? |     254 |
|     2 | ja?     |     148 |
|     3 | wie?    |     141 |
|     4 | echt?   |     128 |
|     5 | hallo?  |     124 |
|     6 | nee?    |     112 |
|     7 | ?       |      88 |
|     8 | waarom? |      80 |
|     9 | oké?    |      78 |



---



### ABA sequence B-word frequencies for language: tr



|   idx | word       |   count |
|------:|:-----------|--------:|
|     0 | ne?        |    4186 |
|     1 | efendim?   |     310 |
|     2 | neden?     |     248 |
|     3 | kim?       |     212 |
|     4 | ?          |     205 |
|     5 | nerede?    |     203 |
|     6 | evet?      |     183 |
|     7 | alo?       |     167 |
|     8 | ha?        |     166 |
|     9 | neredesin? |     160 |



---


Afrikaans seems to have too small a corpus to yield any ABA-sequences, but in all three of the other languages tested here, the highest frequency B-word is the equivalent of "what" (i.e., "wat", "mitä", and "ne" all mean "what").  
Asking "what?" is not an unreasonable way to initiate a repair, but of course we were looking for "huh" equivalents.  
We can try our procedure on English, to see what kind of results we get for the language the majority of subtitles are translated from.


```python
lang = 'en'
display_md(f'### ABA sequence B-word frequencies for language: {lang}')
display_md(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').rename_axis('idx').head(10).to_markdown())
display_md('---')
```


### ABA sequence B-word frequencies for language: en



|   idx | word    |   count |
|------:|:--------|--------:|
|     0 | what?   |   10455 |
|     1 | ?       |    4109 |
|     2 | huh?    |    1988 |
|     3 | yeah?   |    1181 |
|     4 | really? |    1116 |
|     5 | why?    |    1114 |
|     6 | hello?  |     980 |
|     7 | no?     |     779 |
|     8 | okay?   |     737 |
|     9 | who?    |     698 |



---


Even in English "what" is the most frequent B-word, by far.  
However, for English "huh" is the third item; relatively much more frequent than in other languages. Two factors might partially explain why "what" is more prevalent than "huh" in English and even more so in other languages.

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
    display_md(f'### Combined rankings for language: {lang}')
    df = pd.read_csv(f'{lang}_ranks.tsv', sep='\t').rename_axis('idx')
    if len(df) > 0:
        display_md(df.head(10).to_markdown())
    else:
        display_md(f'No combined rankings found for language: {lang}')
    display_md('---')
```


### Combined rankings for language: af



No combined rankings found for language: af



---



### Combined rankings for language: fi



|   idx | word   |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:-------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | häh    |      13 |          0.225935 |       25 |        2 |         27 |
|     1 | nyt    |       7 |          0.247161 |       57 |       18 |         75 |



---



### Combined rankings for language: nl



|   idx | word   |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:-------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | huh    |      33 |          0.159184 |       17 |        0 |         17 |
|     1 | oké    |      78 |          0.202835 |        9 |        9 |         18 |
|     2 | mam    |      28 |          0.202271 |       20 |        8 |         28 |
|     3 | pap    |      23 |          0.211262 |       27 |       13 |         40 |
|     4 | hè     |      13 |          0.181786 |       40 |        5 |         45 |
|     5 | papa   |      14 |          0.218817 |       39 |       19 |         58 |
|     6 | hé     |       8 |          0.180575 |       75 |        4 |         79 |
|     7 | eh     |       7 |          0.213423 |       83 |       15 |         98 |



---



### Combined rankings for language: tr



|   idx | word   |   count |   cosine_distance |   d_rank |   e_rank |   sum_rank |
|------:|:-------|--------:|------------------:|---------:|---------:|-----------:|
|     0 | ha     |     166 |          0.231013 |        8 |        2 |         10 |
|     1 | huh    |      26 |          0.237431 |       27 |        4 |         31 |



---


As we can see, this method yields the correct answer in each language. (We can disregard Afrikaans, because there  were no hits in Afrikaans using the dialogue method.)


```python
# convert this Jupyter notebook to Markdown
import subprocess as sp
make_md = 'jupyter nbconvert universal_huh.ipynb --to markdown --output universal_huh.md'.split(' ')
convert = sp.run(make_md)
if convert.returncode == 0:
    display_md('Jupyter notebook converted to Markdown successfully.')
else:
    display_md('Error: encountered problem converting Jupyter notebook to Markdown')
```


Jupyter notebook converted to Markdown successfully.

