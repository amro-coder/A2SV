class SmallestInfiniteSet:

    def __init__(self):
        self.h=[i for i in range(1,10000)]
        self.exist=set(self.h)
        heapify(self.h)
        
    def popSmallest(self) -> int:
        ans=heappop(self.h)
        self.exist.remove(ans)
        return ans
        

    def addBack(self, num: int) -> None:
        if not num in self.exist:
            self.exist.add(num)
            heappush(self.h,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)