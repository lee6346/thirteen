import models
import game_manager
import utilities

class HandValidator(object):
    
    """
    the card ranks in index 0, 1, ..., 11,  12 are 3, 4, ..., Ace, 2 respectively 
    """
    def __init__(self, high_hand=None, high_class=0):
        self.high_hand = high_hand
        self.high_class = high_class
 
    def is_high_hand(self, hand, hand_manager):
    
        classif = hand_manager.hand_classification(hand)
        standard = self.is_standard_beatable(hand, classif)
        
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
        
        if self.high_hand == None:
            self.high_hand = hand
            self.high_class = classif
            return True
        elif classif == "quad bomb" and hand[0].rank == 12:
            self.high_hand = hand
            self.high_class = classif
            return True
        elif switch.get(classif, False):
            self.high_hand = hand
            self.high_class = classif
            return True
        else:
            return False
        
    def is_standard_beatable(self, hand, classif):
        return self.is_comparable(hand, classif) and self.is_high_value(hand)
        
    def is_comparable(self, hand, classif):
        return self.is_same_length(hand) and self.high_class == classif
        
    def is_high_suit(self, hand):
        return hand[len(hand)-1].suit > self.high_hand[len(hand)-1].suit
        
    def is_high_rank(self, hand):
        return hand[len(hand)-1].rank > self.high_hand[len(hand)-1].rank
            
    def is_same_length(self, hand):
        return len(self.high_hand) == len(hand)
            
    def is_high_value(self, hand):
        return self.is_high_rank(hand) or (hand[len(hand)-1].rank == self.high_hand[len(hand)-1].rank and self.is_high_suit(hand))
      
    def is_playable(self, hand, hand_manager):
        switch = {
            1 : True,
            2 : hand_manager.is_repeated(hand),
            3 : hand_manager.is_repeated(hand) or hand_manager.is_straight(hand),
            4 : hand_manager.is_repeated(hand) or hand_manager.is_straight(hand),
            5 : hand_manager.is_straight(hand),
            6 : hand_manager.is_straight(hand) or hand_manager.is_consecutive_pairs(hand),
            7 : hand_manager.is_straight(hand),
            8 : hand_manager.is_straight(hand) or hand_manager.is_consecutive_pairs(hand),
            9 : hand_manager.is_straight(hand),
            10 : hand_manager.is_straight(hand) or hand_manager.is_consecutive_pairs(hand),
            11 : hand_manager.is_straight(hand),
            12 : hand_manager.is_straight(hand) or hand_manager.is_consecutive_pairs(hand),
        }
        return switch.get(len(hand), False)
      
class HandManager(object):

    def __init__(self):
        pass
    
    def sort_hand(self, hand):
        def cmp_cards(card1, card2):
            if card1.rank > card2.rank:
                return 1
            elif card1.rank == card2.rank and card1.suit > card2.suit:
                return 1
            else:
                return 0
            hand.sort(cmp_cards)
        
    def is_straight(self, hand):
        straight = True
        self.sort_hand(hand)
        for i in range(len(hand)-1):
            if hand[i].rank - hand[i+1].rank != -1:
                straight = False
                break
            elif hand[i].rank == 12:
                straight = False
                break
        return straight
    
    def is_suited(self, hand):
        suited = True
        for i in range(len(hand)-1):
            if hand[i].suit != hand[i+1].suit:
                suited = False
                break
        return suited

    def is_repeated(self, hand):
        repeated = True
        for i in range(len(hand)-1):
            if hand[i].rank != hand[i+1].rank:
                repeated = False
                break
        return repeated
        
    def is_consecutive_pairs(self, hand):
        consec_pair = True
        self.sort_hand(hand)
        if len(hand) % 2 != 0:
            return False
        odd_hand = []
        for i in range(len(hand)/2):
            if hand[2*i] != hand[2*i + 1]:
                consec_pair = False
                break
            odd_hand.append(hand[i*2])
        if not self.is_straight(odd_hand):
            consec_pair = False
        return consec_pair
                   
    def hand_classification(self, hand):
        if len(hand) == 1:
            if hand[0].rank == 12:
                return "single two"
            else:
                return "single"
        elif len(hand) == 2 and self.is_repeated(hand):
            if hand[0].rank == 12:
                return "double two"
            else:
                return "double"
        elif len(hand) >= 3:
            if self.is_repeated(hand) and len(hand) == 3:
                if hand[0].rank == 12:
                    return "triple two"
                else:
                    return "triple"
            elif self.is_straight(hand) and not self.is_suited(hand):
                return "straight"
            elif self.is_straight(hand) and self.is_suited(hand):
                return "suited straight"
            elif len(hand) >= 6 and self.is_consecutive_pairs(hand):
                return "consecutive bomb"
            elif len(hand) == 4 and self.is_repeated(hand):
                return "quad bomb"
        else:
            return 0        
        