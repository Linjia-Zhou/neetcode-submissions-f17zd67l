class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = {}
        res = []

        for i in range(len(s)):
            if s[i] not in end:
                end[s[i]] = len(s) - s[::-1].find(s[i]) - 1
        
        farthest = count = 0
        for i in range(len(s)):
            farthest = max(farthest, end[s[i]])
            count += 1

            if i == farthest:
                res.append(count)
                count = 0
        
        return res



        
        

        




        
