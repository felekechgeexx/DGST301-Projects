import random
from textblob import TextBlob

# Textblob will for my file called "hucklefinn.txt"

# in the same directory as my python notebook or script.

# The text file's contents are stored in the variable "text"
with open('hucklefinn.txt', 'r') as file:
    text = file.read()
    
# This converts the file contents into TextBlob called 
blob = TextBlob(text)

# This creates a list of adjectives and nouns
adjectives = []
nouns = []

# This uses TextBlob to read through the whole text and check fo adjectives and nouns.
# and then adds them to the appropriate list. 
for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)

# This will generate a twenty-line poem using randomly paired adjectives.
# attached with a noun that is randomly generated five times and prints its pairs
for i in range(20):
    a = random.choice(adjectives)
    n = random.choice(nouns)
    print(a,n)   
 
