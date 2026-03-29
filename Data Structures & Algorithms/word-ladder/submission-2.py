from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        count = 1
        d = defaultdict(list)

        temp = wordList[:]
        temp.append(beginWord)

        for word in temp:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                d[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])

        while q:
            for _ in range(len(q)): # must go through every element in the current queue before moving onto newly appended items, otherwise we will double count neighbouring words
                word = q.popleft()

                if word == endWord: return count

                visited.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:] # getting all the patterns this word could be

                    for nei in d[pattern]:
                        if nei not in visited: q.append(nei)

            count += 1

        return 0


