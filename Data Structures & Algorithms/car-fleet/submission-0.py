class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        joined_list = []
        stack = []
        
        for i in range(len(position)):
            joined_list.append([position[i], speed[i]])
        
        for p, s in sorted(joined_list)[::-1]:
            time = (target-p)/s
            
            if len(stack) == 0 or time > stack[-1]: 
                stack.append(time)
        
        return len(stack)

            



        
