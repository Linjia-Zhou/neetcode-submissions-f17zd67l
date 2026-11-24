class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = Counter(c for w in words for c in w)

        # checks if we can move chars and get the same word length for all words[i]
        if sum(d.values()) % len(words) != 0: return False 

        # checks if there are enough values to move around if words not equal
        if sum(d.values()) <= len(words) and len(set(words)) > 1: return False

        return len(set(d.values())) == 1

# [abcdd, abcd, abc]
# {a: 3, b: 3, c: 3, d: 3}