from . import models
from . import game_manager
from . import utilities

class HandValidator(object):
    
    """
    THINGS TO ADJUST
    ?have suits only matter after a specific value? 
    make sure all methods that need sort are sorted_hand
    ?card.rank and card.suit may not be in the correct order
    """
    def __init__(self, high_hand=None, high_class = 0):
        self.high_hand = high_hand
        self.high_class = high_class
 
    def isHighHand(self, hand, hand_manager):
    
        classif = hand_manager.handClassification(hand)
        standard = self.isStandardBeatable(hand, classif)
        
        switch = {
            "single" : standard or classif == "quad bomb",
            "single two" : standard or (classif == "consecutive bomb" and len(card) >= 6) or classif == "quad bomb",
            "double" : standard or classif == "quad bomb",
            "double two" : standard or (classif == "consecutive bomb" and len(card) >= 8) or classif == "quad bomb",
            "triple" : standard or classif == "quad bomb",
            "triple two" : standard or (classif == "consecutive bomb" and len(card) >= 10) or classif == "quad bomb",
            "straight" : standard or classif == "quad bomb",
            "suited straight" : standard or classif == "quad bomb",
            "consecutive bomb" : standard or classif == "quad bomb",
            "quad bomb" : standard,
        }
        
        if self.high_hand = None:
            self.high_hand = hand
            self.high_class = classif
            return True
        elif classif == "quad bomb" and hand[0].rank == 2:
            self.high_hand = hand
            self.high_class = classif
            return True
        elif switch.get(classif, False):
            self.high_hand = hand
            self.high_class = classif
            return True
        else:
            return False
        
    def isStandardBeatable(self, hand, classif):
        if self.isComparable(hand, classif) and self.isHighValue(hand):
            return True
        else:
            return False
        
    def isComparable(self, hand, classif):
        if self.isSameLength(hand) and self.high_class == classif:
            return True
        else:
            return False
        
    def isHighSuit(self, hand):
        if hand[len(hand)-1].suit > self.high_hand[len(hand)-1].suit:
            return True
        else:
            return False
            
    def isSameLength(self, hand):
        if len(self.high_hand) == len(hand):
            return True
        else:
            return False
            
    def isHighValue(self, hand):
        if hand[len(hand)-1].rank > self.high_hand[len(hand)-1].rank:
            return True
        elif hand[len(hand)-1].rank == self.high_hand[len(hand)-1].rank and self.isHighSuit(hand):
            return True
        else:
            return False
      
    #determines if current hand is valid
    def isPlayable(hand, hand_manager):
        switch = {
            1 : True,
            2 : hand_manager.isRepeated(hand),
            3 : hand_manager.isRepeated(hand) or hand_manager.isStraight(hand),
            4 : hand_manager.isRepeated(hand) or hand_manager.isStraight(hand),
            5 : hand_manager.isStraight(hand),
            6 : hand_manager.isStraight(hand) or hand_manager.isConsecutivePairs(hand),
            7 : hand_manager.isStraight(hand),
            8 : hand_manager.isStraight(hand) or hand_manager.isConsecutivePairs(hand),
            9 : hand_manager.isStraight(hand),
            10 : hand_manager.isStraight(hand) or hand_manager.isConsecutivePairs(hand),
            11 : hand_manager.isStraight(hand),
            12 : hand_manager.isStraight(hand) or hand_manager.isConsecutivePairs(hand),
        }
        return switch.get(len(hand), False)
      
class HandManager(object):

    def __init__(self):
        #self.hand = hand
    
    def sortCurrentHand(hand): #must use sort alg
        sorted_hand = []
        for each card in hand:
            sorted_hand.append((hand.getRank(), hand.getSuit()))
        sorted_hand.sort()
        return sorted_hand
        
    def isStraight(self, hand):
        is_straight = True
        sorted_hand = self.sortCurrentHand(hand)
        for i in range(len(sorted_hand-1)):
            if sorted_hand[i].rank - sorted_hand[i+1].rank != 1:
                is_straight = False
                break
            elif sorted_hand[i].rank == 2:
                is_straight = False
                break
        return is_straight
    
    def isSuited(hand):
        is_suited = True
        for i in range(len(hand)-1):
            if hand[i].suit != hand[i+1].suit:
                is_suited = False
                break
        return is_suited

    def isRepeated(hand):
        is_repeated = True
        for i in range(len(hand)-1):
            if hand[i].rank != hand[i+1].rank:
                is_quad = False
                break
        return is_repeated
        
    def isConsecutivePairs(self, hand):
        is_consec_pair = True
        sorted_hand = self.sortCurrentHand(hand)
        for i in range(len(hand)-2):
            if sorted_hand[i*2] != sorted_hand[i*2 + 1]:
                is_consec_pair = False
                break
        if not self.isStraight(subset): # create subset 
            is_consec_pair = False
        return is_consec_pair
                   
    def handClassification(self, hand):
        if len(hand) == 1:
            if hand[0].rank == 2:
                return "single two"
            else:
                return "single"
        elif len(hand) == 2 and self.isRepeated(hand):
            if hand[0].rank == 2:
                return "double two"
            else:
                return "double"
        elif len(hand) >= 3:
            if self.isRepeated(hand) and len(hand) == 3:
                if hand[0].rank == 2:
                    return "triple two"
                else:
                    return "triple"
            elif self.isStraight(hand) and not self.isSuited(hand):
                return "straight"
            elif self.isStraight(hand) and self.isSuited(hand):
                return "suited straight"
            elif len(hand) >= 6 and self.isConsecutivePairs(hand):
                return "consecutive bomb"
            elif len(hand) == 4 and self.is_repeated(hand):
                return "quad bomb"
        else:
            return 0        
        