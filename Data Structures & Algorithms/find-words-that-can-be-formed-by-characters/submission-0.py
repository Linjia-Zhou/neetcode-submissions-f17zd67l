class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        d = Counter(chars)

        for w in words:
            print(f'w: {w}')
            good = True
            chars_set = d.copy()
            print(f'chars_set = {chars_set}')
            for c in w:
                if c not in chars_set or chars_set[c] == 0:
                    good = False
                    break
                else:
                    chars_set[c] -= 1
            
            if good: ans += len(w)
            print(f'chars_set = {chars_set}')
            print(f'ans: {ans}')

        return ans
                    