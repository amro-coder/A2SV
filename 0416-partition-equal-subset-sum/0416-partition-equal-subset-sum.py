class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp=1
        for val in nums:
            dp|=dp<<val
        return ((dp>>(sum(nums)//2))&1) and (not (sum(nums)&1))
        