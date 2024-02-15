class OrderedStream:

    def __init__(self, n: int):
        self.stream=['']*(n+1)
        self.ptr=0

    def insert(self, idKey: int, value: str) -> List[str]:
        ans=[]
        self.stream[idKey-1]=value
        while self.stream[self.ptr]!='':
            ans.append(self.stream[self.ptr])
            self.ptr+=1
        return ans
        
        

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)