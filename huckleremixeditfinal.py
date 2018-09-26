import random
from textblob import TextBlob

# Textblob will for my file called "hucklefinn.txt"

# in the same directory as my python notebook or script.

# The text file's contents are stored in the variable "text"
with open('hucklefinn.txt', 'r') as file:
    text = file.read()
print ("")
    
# This converts the file contents into TextBlob called 
blob = TextBlob(text)
print ("")
  
# This creates a list of adjectives and nouns and verbs
adjectives = []
nouns = []
verbs = []
print ("")
  
# This uses TextBlob to read through the whole text and check fo adjectives, nouns, and verbs
# and then adds them to the appropriate list. 
for word,pos in blob.tags:
    # print(word,pos)
    if (pos == 'JJ'):
        adjectives.append(word)
    if (pos == 'NN'):
        nouns.append(word)
    if (pos == 'VB'):
        verbs.append(word)
print ("")
    
# This will generate a ten-line poem using randomly paired adjectives
# attached with a noun that is randomly generated five times and prints its pairs with the verbs
for i in range(10):
    a1 = random.choice(adjectives)
    a2 = random.choice(adjectives)
    n1 = random.choice(nouns)
    n2 = random.choice(nouns)
    n3 = random.choice(nouns)
    vb = random.choice(verbs)    
    print(n1 + " " + a1 + " " +  vb  + " " + a2  + " " + n3) 
print ("THANK YOU")
    

