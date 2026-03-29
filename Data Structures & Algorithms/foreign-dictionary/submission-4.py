class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        order = {c: set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # invalid b/c if 2 words have same prefix, the longer one should come after the shorter one
                return ''

            for j in range(minLen):
                if w1[j] != w2[j]:
                    order[w1[j]].add(w2[j])
                    break
        
        ans = []
        visited = {}

        def dfs(c):
            if c in visited: return visited[c]

            visited[c] = True

            for nei in order[c]:
                if dfs(nei): return True

            visited[c] = False
            ans.append(c)
        
        for c in order:
            if dfs(c): return ''
            
        ans.reverse()
        return ''.join(ans)
                
        
        

