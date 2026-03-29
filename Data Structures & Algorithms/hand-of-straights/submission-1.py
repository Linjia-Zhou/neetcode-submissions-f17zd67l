class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        hand = sorted(hand)
        m = len(hand) // groupSize
        lst = [[] for _ in range(m)]
        print(hand)
        for num in hand:
            for i in range(m):
                if len(lst[i]) == groupSize: 
                    continue
                elif len(lst[i]) > 0: 
                    if num == lst[i][-1] + 1: 
                        lst[i].append(num)
                        break
                else:
                    lst[i].append(num)
                    break
        
        print(lst)
        for l in lst:
            if len(l) != groupSize: return False
        
        return True




