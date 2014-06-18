# Attempting to build a frequency analyzer for decrypting. Doesn't work.

# Text to encrypt.
text = """hello world". My name is Dan Cole, how are you?"""

text= text.lower()

# Letter frequencies in English.
english = {
' ': 0, 'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.130001, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074
}

def makeKey(text):
    """Create substitution cipher based on last position of char in text."""
    key, n = {}, 0
    for i in text:
        key[i] = str(n)
        n += 1
    return key

def encode(text, key):
    """Encode text with key."""
    encrypted = []
    for i in text:
        encrypted.append(key[i])
    return encrypted

def getFreq(encrypted):
    """Creates a frequency of keys in the table."""
    freq = {}
    for i in encrypted:
        freq[i] = 0
    for i in encrypted:
        freq[i] += 1.0  
    return freq

def freqnorm(freq):
    """Normalizes frequencies as percentage of total."""
    t = 0.0
    for i in freq:
        t += freq[i]
    for i in freq:
        freq[i] /= t
    return freq

def freqScan(keyfreq):
    """Scans a frequency list for a matching letter."""
    diff = compare = 1
    match = ""
    for e in english:
        diff = abs(1 - (1 - english[e]) / (1 - keyfreq))
        #print english[e], keyfreq, compare, diff, e
        if diff < compare:
            compare = diff
            match = e
    return match
    
def makeDecryptKey():
    """Creates decryption key."""
    decryptkey = {}
    for f in freq:
        decryptkey[f] = freqScan(freq[f])
    return decryptkey
    
def printDicts():
    """For debugging, print all dicts."""
    for k in key:
        print k, key[k]
    
    for f in freq:
        print f, freq[f]
    
    for e in english:
        print e, english[e]
        
def decrypt(text, key):
    decrypted = []
    for i in text:
         decrypted.append(key[str(i)])
    return decrypted
        

# First make a key...
key = makeKey(text)

# Then encrypt the text with the key.
encrypted = encode(text, key)

# To decrypt, first get the frequency of the
# values in the encrypted string.
freq = freqnorm(getFreq(encrypted))

# Then compare the values to known English letter frequencies.
decryptkey = makeDecryptKey()

for i in decrypt(encrypted, decryptkey):
    print "".join(i),

#printDicts()