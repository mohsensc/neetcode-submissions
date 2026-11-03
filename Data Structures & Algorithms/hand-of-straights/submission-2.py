from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize:
            return False
        
        hand.sort()
        dic = Counter(hand)

        for i in hand:
            if dic[i] == 0:
                continue
            
            dic[i] -= 1
            j = i + 1
            
            for _ in range(groupSize-1):
                if j in dic and dic[j] > 0:
                    dic[j] -= 1
                    j += 1
                else:
                    return False

        return True