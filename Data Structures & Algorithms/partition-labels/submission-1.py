class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        res = []

        for i in range(len(s)-1, -1, -1):
            if s[i] not in end:
                end[s[i]] = i
        
        farthest = count = 0
        for i in range(len(s)):
            farthest = max(farthest, end[s[i]])
            count += 1

            if i == farthest:
                res.append(count)
                count = 0
        
        return res



        
        

        




        
