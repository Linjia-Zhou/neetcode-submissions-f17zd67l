class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]: return False
        if len(sentence) <= 2: return True

        for i in range(1, len(sentence)-1):
            if sentence[i] == ' ':
                if sentence[i-1] != sentence[i+1]: return False
        
        return True


