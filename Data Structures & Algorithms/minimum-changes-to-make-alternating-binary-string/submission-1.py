class Solution:
    def minOperations(self, s: str) -> int:
        def even_zero(): # s[0] is '0'
            ans = 0
            for i, c in enumerate(s):
                if i % 2 == 0 and c != '0': ans += 1
                if i % 2 == 1 and c != '1': ans += 1 
            return ans

        def odd_zero(): # s[0] is '1'
            ans = 0
            for i, c in enumerate(s):
                if i % 2 == 0 and c != '1': ans += 1
                if i % 2 == 1 and c != '0': ans += 1 
            return ans
        

        return min(even_zero(), odd_zero())


        # 0 1 0 0 0 1 0 0
        # 0 1 2 3 4 5 6 7 
        # even indices need to be 0 if index 0 is 0
        # even = [0, 2, 4, 6], all are 0 so all good
        # odd = [1, 3, 5, 7], index 3 is 0, not 1 so need to change this, ans += 1

        # 0 1 0 0 1 0 0
        # 0 1 2 3 4 5 6
        # q = [3, 6]
        # even = [0, 2, 4, 6], index 4 is 1, not 0, so need to change this. ans += 1
        # odd = [1, 3, 5, 7], index 3 and 5 are 0, not 1, so need to change this. ans += 1