class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans=0
        
        temp=min(k,numOnes)
        ans+=temp
        k-=temp
        
        temp=min(k,numZeros)
        k-=temp
        
        temp=min(k,numNegOnes)
        ans-=temp

        return ans
        
        