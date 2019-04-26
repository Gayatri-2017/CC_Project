# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 11:38:04 2016
@author: Gayatri.K
"""

###### Synonyms ######
import nltk
nltk.download()
from nltk.corpus import wordnet as wn
import textblob
textblob.download()
from textblob import TextBlob

def helloworld():
    print("Hello World!")
    return "apple"

def synonyms(ask):    
    blob = TextBlob(ask)
    y=list()
    for word, pos in blob.tags:
        y.append(pos) #Getting the POS tag of the word
    
    indices = [j for j, i in enumerate(y) if i == 'VB'or i == 'VBZ' or i =='VBP' or i =='VBD' or i == 'VBN'
        or i == 'VBG' or i == 'RB' or i == 'RBR' or i == 'RBS'or i == 'RP'
        or i == 'VP ' or i == 'ADVP' or i == 'ADJP' or i=='JJ' or i == 'JJR' or i == 'JJS'] #Condition if you want to get synonyms only for certain POS and get the indices
        
    z=list()
    for i in indices:
        z.append(blob.words[i]) #Getting words from those indices
        
    def synset(word): #Function to get synonyms
        return wn.synsets(word)
        
    a=list()   
    for i in z:
        a.append(synset(i))
        
    if (len(a)>0): #This whole loop is to get only top 3 synonyms for each word
        b=list()
        for i in range(len(a)):
            if (len(a[i])>=3):
                for j in range(3):
                    b.append( a[i][j])
            
        c=list()
        for i in b: #This loop is to get the actual only synonyms without the extra characters like "synset"
            name, pos, sid = i.name().split('.')
            c.append(name)
        
        d=[c[x:x+3] for x in range(0, len(c),3)] #Grouping each set of 3 synonyms to different groups
        
        for i,j in zip(z,range(len(d))):  #Replacing each word with synonyms keeping rest sentence same
            for k in range(3):  
                yield (ask.replace(i,d[j][k]))
 
<<<<<<< HEAD
# input = "i am not happy"
# print (list(synonyms(input)))
=======
# input = "I am happy"
# print (list(synonyms(input)))
>>>>>>> 09b944fe034484ca1945b9bae3231cdbff08f068
