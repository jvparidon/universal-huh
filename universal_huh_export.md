
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


### ABA sequence B-word frequencies for language: af



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>wat</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



---



### ABA sequence B-word frequencies for language: fi



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>mitä</td>
      <td>1847</td>
    </tr>
    <tr>
      <th>1</th>
      <td>anteeksi</td>
      <td>154</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mikä</td>
      <td>135</td>
    </tr>
    <tr>
      <th>3</th>
      <td>haloo</td>
      <td>127</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kuka</td>
      <td>70</td>
    </tr>
    <tr>
      <th>5</th>
      <td>miksi</td>
      <td>69</td>
    </tr>
    <tr>
      <th>6</th>
      <td>niinkö</td>
      <td>67</td>
    </tr>
    <tr>
      <th>7</th>
      <td>niin</td>
      <td>64</td>
    </tr>
    <tr>
      <th>8</th>
      <td>kuuletko</td>
      <td>62</td>
    </tr>
    <tr>
      <th>9</th>
      <td>kuuletteko</td>
      <td>56</td>
    </tr>
  </tbody>
</table>
</div>



---



### ABA sequence B-word frequencies for language: nl



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>wat</td>
      <td>3058</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pardon</td>
      <td>385</td>
    </tr>
    <tr>
      <th>2</th>
      <td>hallo</td>
      <td>275</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ja</td>
      <td>186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>wie</td>
      <td>175</td>
    </tr>
    <tr>
      <th>5</th>
      <td>echt</td>
      <td>147</td>
    </tr>
    <tr>
      <th>6</th>
      <td>nee</td>
      <td>144</td>
    </tr>
    <tr>
      <th>7</th>
      <td>sorry</td>
      <td>124</td>
    </tr>
    <tr>
      <th>8</th>
      <td>waarom</td>
      <td>115</td>
    </tr>
    <tr>
      <th>9</th>
      <td>jij</td>
      <td>96</td>
    </tr>
  </tbody>
</table>
</div>



---



### ABA sequence B-word frequencies for language: tr



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ne</td>
      <td>7187</td>
    </tr>
    <tr>
      <th>1</th>
      <td>efendim</td>
      <td>559</td>
    </tr>
    <tr>
      <th>2</th>
      <td>neredesin</td>
      <td>409</td>
    </tr>
    <tr>
      <th>3</th>
      <td>neden</td>
      <td>333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pardon</td>
      <td>325</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kim</td>
      <td>287</td>
    </tr>
    <tr>
      <th>6</th>
      <td>alo</td>
      <td>276</td>
    </tr>
    <tr>
      <th>7</th>
      <td>merhaba</td>
      <td>270</td>
    </tr>
    <tr>
      <th>8</th>
      <td>evet</td>
      <td>268</td>
    </tr>
    <tr>
      <th>9</th>
      <td>nerede</td>
      <td>260</td>
    </tr>
  </tbody>
</table>
</div>



---


In every language tested here, the highest frequency B-word is the equivalent of "what" (i.e., "wat", "mitä", and "ne" all mean "what").  
Asking "what?" is not an unreasonable way to initiate a repair, but of course we were looking for "huh" equivalents.  
We can try our procedure on English, to see what kind of results we get for the language the majority of subtitles are translated from.


```python
lang = 'en'
display_md(f'### ABA sequence B-word frequencies for language: {lang}')
print(pd.read_csv(f'dialogue_method/{lang}_freqs.tsv', sep='\t').head().to_markdown())
display_md('---')
```


### ABA sequence B-word frequencies for language: en


|    | word   |   count |
|---:|:-------|--------:|
|  0 | what   |   18991 |
|  1 | nan    |    4145 |
|  2 | huh    |    3229 |
|  3 | hello  |    2167 |
|  4 | really |    1548 |



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
    display(pd.read_csv(f'embedding_method/en-{lang}_muse_neighbors.tsv', sep='\t').head(10))
    display_md('---')
```


### Cross-linguistic cosine distances for language: af



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>cosine_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Hê</td>
      <td>0.219600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>liefie</td>
      <td>0.237689</td>
    </tr>
    <tr>
      <th>2</th>
      <td>nê</td>
      <td>0.238153</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pappatjie</td>
      <td>0.240027</td>
    </tr>
    <tr>
      <th>4</th>
      <td>slivovitz</td>
      <td>0.244561</td>
    </tr>
    <tr>
      <th>5</th>
      <td>my_liefling</td>
      <td>0.247401</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Mammie</td>
      <td>0.249740</td>
    </tr>
    <tr>
      <th>7</th>
      <td>nè</td>
      <td>0.252405</td>
    </tr>
    <tr>
      <th>8</th>
      <td>jou</td>
      <td>0.255947</td>
    </tr>
    <tr>
      <th>9</th>
      <td>my</td>
      <td>0.256397</td>
    </tr>
  </tbody>
</table>
</div>



---



### Cross-linguistic cosine distances for language: fi



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>cosine_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>poju</td>
      <td>0.214634</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kamu</td>
      <td>0.223444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>häh</td>
      <td>0.225935</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ystäväiseni</td>
      <td>0.227547</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kultsi</td>
      <td>0.233309</td>
    </tr>
    <tr>
      <th>5</th>
      <td>pikkukaveri</td>
      <td>0.233730</td>
    </tr>
    <tr>
      <th>6</th>
      <td>helkkari</td>
      <td>0.234174</td>
    </tr>
    <tr>
      <th>7</th>
      <td>pikkumies</td>
      <td>0.235422</td>
    </tr>
    <tr>
      <th>8</th>
      <td>helkkarin</td>
      <td>0.235567</td>
    </tr>
    <tr>
      <th>9</th>
      <td>herraseni</td>
      <td>0.239839</td>
    </tr>
  </tbody>
</table>
</div>



---



### Cross-linguistic cosine distances for language: nl



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>cosine_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>huh</td>
      <td>0.159184</td>
    </tr>
    <tr>
      <th>1</th>
      <td>schatje</td>
      <td>0.162617</td>
    </tr>
    <tr>
      <th>2</th>
      <td>lieverd</td>
      <td>0.174831</td>
    </tr>
    <tr>
      <th>3</th>
      <td>liefje</td>
      <td>0.178294</td>
    </tr>
    <tr>
      <th>4</th>
      <td>hé</td>
      <td>0.180575</td>
    </tr>
    <tr>
      <th>5</th>
      <td>hè</td>
      <td>0.181786</td>
    </tr>
    <tr>
      <th>6</th>
      <td>makker</td>
      <td>0.187827</td>
    </tr>
    <tr>
      <th>7</th>
      <td>meneertje</td>
      <td>0.194914</td>
    </tr>
    <tr>
      <th>8</th>
      <td>mam</td>
      <td>0.202271</td>
    </tr>
    <tr>
      <th>9</th>
      <td>oké</td>
      <td>0.202835</td>
    </tr>
  </tbody>
</table>
</div>



---



### Cross-linguistic cosine distances for language: tr



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>cosine_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>dostum</td>
      <td>0.217794</td>
    </tr>
    <tr>
      <th>1</th>
      <td>&lt;/s&gt;</td>
      <td>0.226429</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ha</td>
      <td>0.231013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ahbap</td>
      <td>0.232770</td>
    </tr>
    <tr>
      <th>4</th>
      <td>huh</td>
      <td>0.237431</td>
    </tr>
    <tr>
      <th>5</th>
      <td>adamım</td>
      <td>0.239443</td>
    </tr>
    <tr>
      <th>6</th>
      <td>koca_oğlan</td>
      <td>0.242911</td>
    </tr>
    <tr>
      <th>7</th>
      <td>tatlım</td>
      <td>0.247647</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Hey</td>
      <td>0.250283</td>
    </tr>
    <tr>
      <th>9</th>
      <td>beyler</td>
      <td>0.253327</td>
    </tr>
  </tbody>
</table>
</div>



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
    display(pd.read_csv(f'{lang}_ranks.tsv', sep='\t').head(10))
    display_md('---')
```


### Combined rankings for language: af



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
      <th>cosine_distance</th>
      <th>d_rank</th>
      <th>e_rank</th>
      <th>sum_rank</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



---



### Combined rankings for language: fi



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
      <th>cosine_distance</th>
      <th>d_rank</th>
      <th>e_rank</th>
      <th>sum_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>häh</td>
      <td>17</td>
      <td>0.225935</td>
      <td>24</td>
      <td>2</td>
      <td>26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nyt</td>
      <td>7</td>
      <td>0.247161</td>
      <td>75</td>
      <td>18</td>
      <td>93</td>
    </tr>
    <tr>
      <th>2</th>
      <td>kultaseni</td>
      <td>5</td>
      <td>0.245345</td>
      <td>96</td>
      <td>13</td>
      <td>109</td>
    </tr>
  </tbody>
</table>
</div>



---



### Combined rankings for language: nl



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
      <th>cosine_distance</th>
      <th>d_rank</th>
      <th>e_rank</th>
      <th>sum_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>huh</td>
      <td>51</td>
      <td>0.159184</td>
      <td>15</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>oké</td>
      <td>88</td>
      <td>0.202835</td>
      <td>11</td>
      <td>9</td>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mam</td>
      <td>37</td>
      <td>0.202271</td>
      <td>19</td>
      <td>8</td>
      <td>27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>papa</td>
      <td>41</td>
      <td>0.218817</td>
      <td>17</td>
      <td>19</td>
      <td>36</td>
    </tr>
    <tr>
      <th>4</th>
      <td>pap</td>
      <td>30</td>
      <td>0.211262</td>
      <td>26</td>
      <td>13</td>
      <td>39</td>
    </tr>
    <tr>
      <th>5</th>
      <td>hè</td>
      <td>21</td>
      <td>0.181786</td>
      <td>39</td>
      <td>5</td>
      <td>44</td>
    </tr>
    <tr>
      <th>6</th>
      <td>schatje</td>
      <td>13</td>
      <td>0.162617</td>
      <td>58</td>
      <td>1</td>
      <td>59</td>
    </tr>
    <tr>
      <th>7</th>
      <td>hé</td>
      <td>13</td>
      <td>0.180575</td>
      <td>63</td>
      <td>4</td>
      <td>67</td>
    </tr>
    <tr>
      <th>8</th>
      <td>lieverd</td>
      <td>10</td>
      <td>0.174831</td>
      <td>93</td>
      <td>2</td>
      <td>95</td>
    </tr>
    <tr>
      <th>9</th>
      <td>eh</td>
      <td>7</td>
      <td>0.213423</td>
      <td>136</td>
      <td>15</td>
      <td>151</td>
    </tr>
  </tbody>
</table>
</div>



---



### Combined rankings for language: tr



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>word</th>
      <th>count</th>
      <th>cosine_distance</th>
      <th>d_rank</th>
      <th>e_rank</th>
      <th>sum_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ha</td>
      <td>233</td>
      <td>0.231013</td>
      <td>11</td>
      <td>2</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tatlım</td>
      <td>78</td>
      <td>0.247647</td>
      <td>20</td>
      <td>7</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>huh</td>
      <td>49</td>
      <td>0.237431</td>
      <td>27</td>
      <td>4</td>
      <td>31</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bebeğim</td>
      <td>15</td>
      <td>0.255516</td>
      <td>104</td>
      <td>11</td>
      <td>115</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ahbap</td>
      <td>5</td>
      <td>0.232770</td>
      <td>459</td>
      <td>3</td>
      <td>462</td>
    </tr>
    <tr>
      <th>5</th>
      <td>kanka</td>
      <td>3</td>
      <td>0.262215</td>
      <td>727</td>
      <td>13</td>
      <td>740</td>
    </tr>
    <tr>
      <th>6</th>
      <td>dostum</td>
      <td>2</td>
      <td>0.217794</td>
      <td>1259</td>
      <td>0</td>
      <td>1259</td>
    </tr>
  </tbody>
</table>
</div>



---


As we can see, this method yields the correct answer in every language but Afrikaans, because the only hit in Afrikaans using the dialogue method was "wat" and that word isn't present in the top 100 of cross-linguistic nearest neighbors for Afrikaans.
