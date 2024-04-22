class DataStream:

    def __init__(self, value: int, k: int):
        self.val=value
        self.k=k
        self.left=k
        
    def consec(self, num: int) -> bool:
        if num==self.val:
            self.left=max(0,self.left-1)
        else:
            self.left=self.k
        return self.left==0
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)