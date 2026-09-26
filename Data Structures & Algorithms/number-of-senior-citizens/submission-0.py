class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0

        for d in details:
            if int(d[-4:-2]) > 60: ans += 1

        return ans 