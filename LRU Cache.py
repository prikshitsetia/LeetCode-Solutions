class LRUCache:
    def __init__(self, capacity: int):
        
        self.capacity=capacity
        self.di={}
        self.li=[]
        
    def get(self, key: int) -> int:
        if key in self.di.keys():
            self.li.remove(key)
            self.li.append(key)
            return self.di[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.di.keys():
            if len(self.li)==self.capacity:
                del self.di[self.li.pop(0)]
        else:
            self.li.remove(key)
        self.di[key]=value
        self.li.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)