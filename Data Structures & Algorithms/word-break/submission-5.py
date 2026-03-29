class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]: # we found a match, so don't need to go through any more words in wordDict
                    break
        
        return dp[0]

                




