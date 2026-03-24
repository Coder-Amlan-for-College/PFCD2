import random
from enum import Enum

class Suit(Enum):
    HEARTS="Hearts"
    DIAMONDS="Diamonds"
    CLUBS="Clubs"
    SPADES="Spades"

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def value(self):
        if self.rank in ['J','Q','K']:
            return 10
        elif self.rank=='A':
            return 11
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit.value}"

class Deck:
     def __init__(self):
         self.cards=[]
         self.build_deck()

     def build_deck(self):
         ranks=['2','3','4','5','6','7','8','9','10','J','Q','K', 'A']

         for suit in Suit:
             for rank in ranks:
                 self.cards.append(Card(suit,rank))

     def shuffle(self):
         random.shuffle(self.cards)

     def draw_card(self):
         return self.cards.pop()


class Player:
    def __init__(self,name):
        self.name=name
        self.hand=[]
        self.standing=False
    
    def add_card(self,card):
        self.hand.append(card)
    
    def calculate_total(self):
        total = sum(card.value() for card in self.hand)
        aces = sum()