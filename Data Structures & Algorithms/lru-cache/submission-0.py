from collections import defaultdict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict() # key: node
        self.head, self.tail = Node(-1, -1), Node(-1, -1) # dummy head, dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def insert(self, node): # always insert right after head
        curr_head_next = self.head.next
        curr_head_next.prev = self.head.next = node

        node.prev = self.head
        node.next = curr_head_next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            del self.cache[self.tail.prev.key]
            self.remove(self.tail.prev)

        print(self.cache)
        print(self.tail.prev)
        
