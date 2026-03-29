from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            #key = ''.join(sorted(word))
            #hm[key].append(word)

            counts = [0] * 26

            for character in word:
                index = ord(character) - ord('a')
                counts[index] += 1

            key = tuple(counts)
            hm[key].append(word)
        
        return hm.values()
        
        
