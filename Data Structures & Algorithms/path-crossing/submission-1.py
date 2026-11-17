class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0, 0]
        sett = {(0, 0)}

        for c in path:
            if c == 'N':
                curr[1] += 1
            elif c == 'S': 
                curr[1] -= 1
            elif c == 'E': 
                curr[0] += 1
            else: 
                curr[0] -= 1
            
            if tuple(curr) in sett: return True
            else: sett.add(tuple(curr))
        
        return False

            