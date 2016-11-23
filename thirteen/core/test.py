import models
import game_logic


deck = models.Deck()

validator = game_logic.HandValidator()
manager = game_logic.HandManager()


    

"""
Testing is_straight and suits
"""
#standard suited straight 7 to 11
hand = []
for i in range(5):
    hand.append(models.Card(0, i+7))

for card in hand:
    print card.rank, card.suit

print manager.is_straight(hand)    
print manager.is_suited(hand)
print manager.hand_classification(hand)
print validator.is_playable(hand, manager)

"""
Testing is repeated and consecs
"""
hand2 = []
hand2.append(models.Card(0, 9))
hand2.append(models.Card(1, 9))
hand2.append(models.Card(0, 10))
hand2.append(models.Card(1, 10))
hand2.append(models.Card(0, 11))
hand2.append(models.Card(1, 11))
hand2.append(models.Card(0, 12))
hand2.append(models.Card(1, 12))
for card in hand2:
    print card.rank, card.suit
print manager.is_consecutive_pairs(hand2)
print manager.hand_classification(hand2)
print validator.is_playable(hand2, manager)

"""
Testing 3
"""
hand3 = []
hand3.append(models.Card(0, 1))
hand3.append(models.Card(0, 2))
print validator.is_playable(hand3, manager)


"""
testing is_high_hand
"""
hand4 = []
hand5 = []
hand6 = []
print "\nTESTING HIGH HAND\n"
print validator.high_hand, validator.high_class
hand4.append(models.Card(2, 12))
print validator.is_high_hand(hand4, manager)
print validator.high_hand, validator.high_class
hand5.append(models.Card(3, 12))
print validator.is_high_hand(hand5, manager)
print validator.high_hand, validator.high_class
hand6.append(models.Card(0, 9))
hand6.append(models.Card(1, 9))
hand6.append(models.Card(0, 10))
hand6.append(models.Card(1, 10))
hand6.append(models.Card(0, 11))
hand6.append(models.Card(1, 11))
print validator.is_high_hand(hand6, manager)
print validator.high_hand, validator.high_class