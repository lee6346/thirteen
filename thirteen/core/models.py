
import random

class Card(object):
    """
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    ranks = ["Aces", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "Jack", "Queen", "King"]
    """ 
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    
    def getSuit(self):
        return self.suit
        
    def setSuit(self, index):
        self.suit = index
    
    def getRank(self):
        return self.rank
        
    def setRank(self, index):
        self.rank = index
        
class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(0, 13):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def reset(self):
        #self.__init__() not working..
        self.cards = []
        for suit in range(4):
            for rank in range(0, 13):
                card = Card(suit, rank)
                self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def pop_card(self):
        self.cards.pop(-1)
    
    def deal_cards(self, num_players, num_iterations, ):
        #initialize empty list of lists
        hands = []
        for i in range(num_players)
            hands.append([])
        reset(self)
        shuffle(self)
        for i in range(13):
            for j in range(num_players):
                hands[j].append(pop_card(self))
        return hands
        