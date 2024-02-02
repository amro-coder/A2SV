class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans+=nums[i]==nums[j]
        return ans
        