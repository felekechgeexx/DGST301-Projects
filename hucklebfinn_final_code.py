import random
from textblob import TextBlob

with open('hucklefinn.txt', 'r') as file:
    text = file.read()

blob = TextBlob(text)

adjectives = []
nouns = []

for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)

for i in range(30):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n) 
