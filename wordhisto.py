# This code takes user-defined text and produces a normalized,
# visual representation of the character and word counts in the text.

import string

def makeDict(text):
    """Creates a dictionary of items in the text."""
    itemlist = {}
    for i in text:
        itemlist[i] = 0
    return text, itemlist
    
def getFreqs(text, itemlist):
    """Updates the dictionary with item counts."""
    for i in text:
        itemlist[i] = itemlist[i] + 1
    return itemlist

def sortFreqs(itemlist):
    """Sort the dictionary from most to least frequent item."""
    orderedItems = []
    for i in itemlist:
        orderedItems.append((itemlist[i], i))
    orderedItems = sorted(orderedItems)[::-1]
    return orderedItems
    
def makeHisto(textcount):
    """Turns frequency into histogram."""
    maxfreq = textcount[0][0]
    minfreq = textcount[len(textcount) - 1][0]
    normsize = 40.0 # Use this number for max histo size.
    for i in textcount:
        histo = int(((i[0] - minfreq) * (normsize)) \
        / (maxfreq - minfreq + 1) + 1.0) * "*" 
        print i[1].upper() + " " * (10-len(i[1])), histo

def charFreq(text):
    """Print the character frequency in a string."""
    print "Character Frequency"
    print "------ ---------"
    textcount = sortFreqs(getFreqs(makeDict(text)[0], makeDict(text)[1]))    
    makeHisto(textcount)

def wordFreq(text):
    """Print the word frequency in a string."""
    print "Word Frequency"
    print "---- ---------"
    text = text.split(" ")
    text = [''.join(x for x in x if x not in string.punctuation) for x in text] # Remove punctuation.
    textcount = sortFreqs(getFreqs(makeDict(text)[0], makeDict(text)[1]))    
    makeHisto(textcount)

# Get user's text and print results.        
text = raw_input("Enter text > ").lower()    
charFreq(text)
wordFreq(text)


