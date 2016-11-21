"""
class Utilities(object):

    def __init__(self):
        pass

    def insert_sort(self, hand):
        for i in range(1, len(hand)):
            currentcard = hand[i]
            position = i

            while position > 0 and hand[position-1].rank > currentcard.rank:
                hand[position]=hand[position-1]
                position = position-1

            hand[position] = currentcard

    def insertionSort(self, alist):
        for index in range(1,len(alist)):

            currentvalue = alist[index]
            position = index

            while position>0 and alist[position-1]>currentvalue:
                alist[position]=alist[position-1]
                position = position-1

            alist[position]=currentvalue


"""