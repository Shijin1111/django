from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        # mycards = [(s,r) for s in SUITE for r in RANKS] did'nt understand.
        for r in RANKS:
            for s in SUITE:
                self.allcards.append((s,r))
    def suffle(self):
        shuffle(self.allcards)
    def split(self):
        return (self.allcards[0:26],self.allcards[26:52])

class Hands:
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return "contains",len(self.cards),"cards"
    def add(self,added_cards):
        self.add.extend(added_cards)
    def remove_cards(self):
        return self.cards.pop()
    
class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card=self.hand.remove_cards()
        print("{} has placed {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_cards(self):
        war_cards = []
        for x in range (3):
            war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        return len(self.hand.cards) != 0

print("welcome to war,let's begin...")
d=Deck()
d.shuffle()
half1,half2=d.split_in_half()
comp=Player("computer",Hands((half1)))
name=input("what is your name?")
user=Player(name,Hands(half2))
total_rounds=0
war_count=0

while user.still_has_cards() and comp.still_had_cards():
    total_rounds+=1
    print("tie for a new round")
    print("here are the currrent standings")
    print(user.name+"has the count:"+str(len(user.hand.cards)))
    print(comp.name+"has the count:"+str(len(comp.hand.cards)))
    print("play the cards!")
    print("\n")
    table_cards=[]
    c_card=comp.play_card()
    p_card=user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)
    if c_card[1] == p_card[1]:
        war_count += 1
        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print("game over,number of rounds:"+str(total_rounds))
print("a war happened"+str(war_count)+"times")