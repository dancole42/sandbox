# This code takes user-defined text and produces a normalized,
# visual representation of the letter count in the text.

def makeDict(text):
    """Creates a lowercase dictionary of letters in the text."""
    letterlist = {}
    for letter in text.lower():
        letterlist[letter] = 1
    return text.lower(), letterlist
    
def getFreqs(text, letterlist):
    """Updates the dictionary with letter counts."""
    for letter in text:
        letterlist[letter] = letterlist[letter] + 1
    return letterlist

def sortFreqs(letterlist):
    """Sort the dictionary from most to least frequent letter."""
    orderedLetters = []
    for letter in letterlist:
        orderedLetters.append((letterlist[letter], letter))
    orderedLetters = sorted(orderedLetters)[::-1]
    return orderedLetters
    
def makeHisto(lettercount):
    """Turns frequency into histogram."""
    maxfreq = lettercount[0][0]
    minfreq = lettercount[len(lettercount) - 1][0]
    normsize = 40.0 # Use this number for max histo size.
    for letter in lettercount:
        histo = int(((letter[0] - minfreq) * (normsize)) \
        / (maxfreq - minfreq) + 1.0) * "*" 
        print letter[1].upper(), histo
        
text = raw_input("Enter text > ")    
lettercount = sortFreqs(getFreqs(makeDict(text)[0], makeDict(text)[1]))    
makeHisto(lettercount)