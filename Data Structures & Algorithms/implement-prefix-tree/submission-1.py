class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for ch in word:
            index = ord(ch) - ord('a')
            
            if curr.children[index] is None:
                new_node = TrieNode()
                curr.children[index] = new_node
            
            curr = curr.children[index]
        
        curr.endOfWord = True
        
    def search(self, word: str) -> bool:
        curr = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if curr.children[index] is None:
                return False
            else:
                curr = curr.children[index]

        return curr.endOfWord    

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for ch in prefix:
            index = ord(ch) - ord('a')

            if curr.children[index] is None:
                return False
            else:
                curr = curr.children[index]
        
        return True
        
        