class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans=sum(piles)
        h=[]
        for i in range(len(piles)):
            heappush(h,-piles[i])
        for _ in range(k):
            val=-heappop(h)
            temp=val//2
            ans-=temp
            val-=temp
            heappush(h,-val)
        return ans
        
        