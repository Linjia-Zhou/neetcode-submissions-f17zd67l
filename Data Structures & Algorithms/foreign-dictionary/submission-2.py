class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # post-order dfs
        
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # invalid b/c if 2 words have same prefix, the longer one should come after the shorter one
                return ''

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    # we break after first instance of difference b/c alphabetical sorting is only guaranteed up till this point
                    # ex. in english, "dim" comes before "dog" because "i" comes before "m"
                    # so, it would be incorrect to assume "m" comes before "g" (notably, "m" does NOT come before "g" in english alphabet) 
                    break 
        
        visited = {} # {character: T/F}, F means we've visited this char, T means this char is in our current path
        ans = []

        def dfs(c):
            if c in visited: # detected a cycle
                return visited[c]

            visited[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
            
            visited[c] = False
            ans.append(c)
        
        for c in adj:
            if dfs(c): # detected a cycle
                return ''

        ans.reverse()
        return ''.join(ans)
            
