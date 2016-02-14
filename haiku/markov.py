from textblob import TextBlob
from nltk.tokenize import BlanklineTokenizer
import random

with open('basho.txt', 'r') as content_file:
    content = content_file.read()

#print content

tokenizer = BlanklineTokenizer()
cleaned_content = content.lower()
corpus = TextBlob(cleaned_content,  tokenizer=tokenizer)

haiku = corpus.sentences
#print haiku

bigrams = corpus.ngrams(n=2)
trigrams = corpus.ngrams(n=3)

#print bigrams
dict = {}
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

#print dict

def weighted_choice(map):
    choices = [] 
    for k in map:
        #print k 
        for n in range(1, map[k] + 1):
            choices.append(k)
    #print choices
    choice = random.choice(choices)
    #print choice
    return choice

seed = random.choice(dict.keys())
length = random.randint(11,15) 

output = [seed]
#print output
for i in range(length):
    output.append(weighted_choice(dict[output[i]]))

print output[0:4]
print output[4:9]
print output[9:]




