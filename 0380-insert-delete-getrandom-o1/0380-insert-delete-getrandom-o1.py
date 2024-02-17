class RandomizedSet:

    def __init__(self):
        self.elements=set()
        
    def insert(self, value: int) -> bool:
        if value in self.elements:
            return False
        self.elements.add(value)
        return True

    def remove(self, value: int) -> bool:
        if value not in self.elements:
            return False
        self.elements.remove(value)
        return True
                

    def getRandom(self) -> int:
        return list(self.elements)[randint(0,len(self.elements)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()