class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans,current_sum=0,0
        for i in range(len(nums)):
            current_sum+=nums[i]
            current_sum=max(current_sum,0)
            ans=max(ans,current_sum)
        return ans if ans>0 else max(nums)
        