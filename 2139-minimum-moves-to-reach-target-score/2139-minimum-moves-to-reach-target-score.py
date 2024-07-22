class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans=0
        while target>1 and maxDoubles>0:
            ans+=(target&1)+1
            maxDoubles-=1
            target//=2
        return ans+target-1
            
            
        