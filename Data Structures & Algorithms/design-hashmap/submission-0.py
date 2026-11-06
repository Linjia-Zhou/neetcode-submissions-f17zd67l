class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        found = False
        for lst in self.hashmap:
            if lst[0] == key:
                if len(lst) == 1:
                    lst.append(value)
                else:
                    lst[1] = value
                
                found = True
        
        if not found: self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for lst in self.hashmap:
            if len(lst) == 2 and lst[0] == key: return lst[1]
        
        return -1

    def remove(self, key: int) -> None:
        for lst in self.hashmap:
            if lst[0] == key:
                self.hashmap.remove(lst)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)