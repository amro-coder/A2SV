class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans,j,product=0,0,1
        for i in range(len(nums)):
            j=max(j,i)
            while j<len(nums) and nums[j]*product<k:
                product*=nums[j]
                j+=1
            ans+=j-i
            if j>i:
                product//=nums[i]
        return ans
        
        