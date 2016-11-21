from . import models
from . import game_manager
from . import utilities

public class HandValidator(object):
    
    """
    RANKING AND COMPARING HANDS
    we use (rank, isConsecutive, isBomb) 3-tuple structure to determine hand_types 
    ranks:                  isConsecutive:              isBomb              isSuited
    0 = null                0 = false                   0 = false           0 = false
    1 = single              1 = true                    1 = true            1 = true
    2 = pair
    3 = triple
    4 = quad 
    def(length)
    """
    def __init__(self, high_hand=None, player=0, hand_type = (0, 0)):
        self.high_hand = high_hand
        self.player_number = player
        self.hand_type = hand_type 
        
    def setHighHand(self, hand, player):
        self.high_hand = hand
        self.player_number = player
        self.hand_type = getHandType(hand)
        
    #store hand into a list of tuples, sort, and return      
    def sortCurrentHand(self, hand):
        sorted_hand = []
        for each card in hand:
            sorted_hand.append((hand.getRank(), hand.getSuit()))
        sorted_hand.sort()
        return sorted_hand
    
    #compares high hand with current hand
    def isHighHand(hand):
        hand_rank = getHandType(hand)
    
    #4 2's automatically wins   
    def auto_win_hand(hand):
        if getHandType(hand) == (4, 0) && getHandType(hand)[0] == 2: #mod 3?
            return True
        return False
        
    #determines if current hand is valid and sets new high hand if true 
    def isValidHand(self, hand):
        hand_type = getHandType(hand)
        if hand_type[0] == 0:
            return False
        #if high hand is also 4 of kind, comparison function is used
        elif hand_type == (4, 0):
            if self.hand_type = (4, 0):
                return isHighHand(hand_type)
            else
                return True
        elif hand_type == ()
              
            
        if hand_type == (4, 0) and hand[0].getRank()#mod 3? == high:
            return True
        elif isHighHand(hand_type):
            return True
        if len(hand) == len(self.high_hand) and 
        "if get type matches the high_hand and it's of higher or equal value, then good to go"
        """
         if getHandType(hand) == self.
        
        """
    # returns the hand type tuple (see above structure)   
    def getHandType(self, hand):
        sorted_hand = sortCurrentHand(hand)
        #dictionary for switch-case return value
        switch = {
            0 : (0, 0),
            1 : (1, 0),
            2 : two_card_type(sorted_hand),
            3 : three_card_type(sorted_hand),
            4 : four_card_type(sorted_hand),
        }
        return switch.get(len(sorted_hand), default_card_type(sorted_hand))
        
    def two_card_type(hand):
        if hand[0][0] == hand[1][0]:
            return (2, 0)
        return (0, 0)
        
    def three_card_type(hand):
        if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0]:
            return (3, 0)
        elif is_consecutive(hand, len(hand), 1)
            return (3, 1)
        return (0, 0)
        #don't need length as parameter?
    def four_card_type(hand):
        if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[2][0] == hand[3][0]:
            return (4, 0)
        elif is_consecutive(hand, len(hand), 1):
            return (4, 1)
        return (0, 0)
        
    def default_card_type(hand):
        if len(hand) % 2 != 0:
            
            
    def is_consecutive(hand, length, freq):
        consecutive = True
        if freq == 1:
            for i in range(len(hand)-1):
                if hand[i][0] - hand[i+1][0] != 1:
                    consecutive = False
                    break
        elif freq == 2:
            for i in range(len(hand)/2-1):
                if (hand[i*freq][0] - hand[(i+1)*freq][0] != 1) or (hand[i*freq][0] != hand[i*freq + 1][0]):
                    consecutive = False
                    break
        return consecutive
        
        