class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        for i in range(1,len(piles)//3+1):
            ans+=piles[len(piles)-2*i]
        return ans