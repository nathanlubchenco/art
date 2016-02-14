from textblob import TextBlob
from nltk.tokenize import BlanklineTokenizer

with open('basho.txt', 'r') as content_file:
    content = content_file.read()

#print content

tokenizer = BlanklineTokenizer()
corpus = TextBlob(content,  tokenizer=tokenizer)

haiku = corpus.sentences
#print haiku

bigrams = corpus.ngrams(n=2)
trigrams = corpus.ngrams(n=3)

#print bigrams

for bigram in bigrams:
    k = bigram[0]
    v = bigram[1]
    if k in dict:
        if v in dict[k]:
            dict[k][v] = dict[k][v] + 1
        else:
            dict[k][v] = 1
    else:
        dict[k] = { v : 1}

print dict
