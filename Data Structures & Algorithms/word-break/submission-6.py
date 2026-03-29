class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        trues = [len(s)] # list of all indices that are true

        for i in range(len(s)-1, -1, -1):
            for j in trues:
                if dp[i]: break
                if s[i:j] in wordDict:
                    dp[i] = True
                    trues.append(i)
        
        return dp[0]