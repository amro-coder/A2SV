class RandomizedSet:

    def __init__(self):
        self.elements=[]
        self.index=defaultdict(lambda :-1)
        

    def insert(self, value: int) -> bool:
        if self.index[value]==-1:
            self.index[value]=len(self.elements)
            self.elements.append(value)
            return True
        return False

    def remove(self, value: int) -> bool:
        if self.index[value]==-1:
            return False
        
        temp_index =self.index[value]
        temp_value=self.elements[-1]
        self.elements[self.index[value]],self.elements[-1]=self.elements[-1],self.elements[self.index[value]]
        self.elements.pop()
        
        self.index[temp_value]=temp_index
        self.index[value]=-1
        return True
                

    def getRandom(self) -> int:
        return self.elements[randint(0,len(self.elements)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()