# Deck of playing cards

from random import randint, shuffle

class Deck(object):
    
    def __init__(self):
        self.deck_cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = suit, rank
                self.deck_cards.append(card)             

    def shuffle_deck(self):
        shuffle(self.deck_cards)

class Cards(object):
    suit_names = ["spades", "hearts", "clubs", "diamonds"]
    rank_names = ["ace", "jack", "queen", "king"]

    for i in range (2,11):
        rank_names.insert(i-1, str(i))
        
def your_card(deck, i):
    your_card = deck.deck_cards[(i-1)]
    return your_card

def print_deck(deck):
    for your_card in deck.deck_cards:
        print_card(your_card)
    
def print_card(your_card, message="Card: "):
    print "%s %s of %s" % (message, Cards.rank_names[(your_card[1])-1],  Cards.suit_names[(your_card[0])-1])

my_deck = Deck()
my_deck.shuffle_deck()

linelength = 40

def TopLine():
    print "-" * linelength
    print "=" * linelength

def BottomLine():
    print "=" * linelength
    print "-" * linelength

# Print the whole deck
TopLine()
print "           THE FULL DECK              "
BottomLine()
print_deck(my_deck)

# Pick a random card
TopLine()
print_card(your_card(my_deck, randint(0,51)), "Random Card:")
BottomLine()
