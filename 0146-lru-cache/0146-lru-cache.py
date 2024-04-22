class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.val={}
        self.lru=deque()
        self.last={}
        self.current=0

    def get(self, key: int) -> int:
        if key in self.val:
            self.last[key]=len(self.lru)
            self.lru.append(key)
            return self.val[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if not(key in self.val or len(self.val)<self.capacity):
            while self.last[self.lru[self.current]]!=self.current:
                self.current+=1
            removedKey=self.lru[self.current]
            self.current+=1
            del self.val[removedKey]
            
        self.val[key]=value
        self.last[key]=len(self.lru)
        self.lru.append(key)
            
        
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)