<<<<<<< HEAD
numbers = [1, 2, 3, 4, 5]
numbers.insert(0,65)
print(numbers)
=======
from random import shuffle
import random
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    # """
    # This is the Deck Class. This object will create a deck of cards to initiate
    # play. You can then use this Deck list of cards to split in half and give to
    # the players. It will use SUITE and RANKS to create the deck. It should also
    # have a method for splitting/cutting the deck in half and Shuffling the deck.
    # """
deck=[]
for i in range (4):
    for j in range (13):
        deck.append(SUITE[i]+RANKS[j])
c=[]
for i in range (52) :
    c.append(random.choice(deck))#but can use shuffle(deck) method
comp_cards=c[0:26]
user_cards=c[26:52]
print(user_cards)
print(comp_cards)
shuffle(user_cards)
shuffle(comp_cards)


>>>>>>> e7626f0f2e7c49f92defc117dc3b994f83b6b869
