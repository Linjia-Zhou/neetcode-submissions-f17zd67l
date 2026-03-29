class TrieNode:
    def __init__(self):
        self.children = {} 
        # ex, {a: TrieNode}
        # key is string, value is TrieNode that will hold its own children dictionary, 
        # which will include all letters that can be obtained from key

        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word): # reached the end of the word we're looking for
                return root.endOfWord # if there are still more letters remaining in our tree, then we need to return False
            
            if word[i] == '.': # need to check every single child in root 
                for letter_node in root.children.values():
                    if dfs(i+1, letter_node):
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(i+1, root.children[word[i]])
        
        return dfs(0, self.root)



