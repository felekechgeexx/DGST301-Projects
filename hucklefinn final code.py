import random

from textblob import TextBlob

# This looks for a file called "huclefinn.txt"

# in the same directory as my python notebook or script.


# The text file's contents are stored in the variable "text"


with open ('huclefinn.txt' , 'r') as file:
    text = file.read() 


# This parses the text file contents into a TextBlob object called "blob"
blob = TextBlob(text)


# Create two empty lists for storing adjectives and nouns
adjectives = [] 
nouns = [] 

# TextBlob parses the words and labels them with a part-of-speech tag.

# This code loops through the whole text, checks for adjectives and nouns

# and adds them to the appropriate list.

for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'): 
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word) 


# This generates a thirty-line poem by pairing a random adjective 


# with a random noun five times and printing the pairs.



with open('huclefinn.txt' , 'r') as file:
    text = file.read() 


wordlist = text.split("len")


len(wordlist) 


print(random.choice(wordlist))


blob.tags


for i in range(30):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n)  


print(nouns) 



print(adjectives) 

