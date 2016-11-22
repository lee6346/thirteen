import random

class Card(object):

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
        
class Deck(object):

    def __init__(self):
        self.reset()
    
    def reset(self):
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def pop_card(self):
        return self.cards.pop(-1)
    
    def deal_cards(self, num_players, num_iterations):
        hands = []
        for i in range(num_players):
            hands.append([])
        self.reset()
        self.shuffle()
        for i in range(13):
            for j in range(num_players):
                hands[j].append(self.pop_card())
        return hands
        