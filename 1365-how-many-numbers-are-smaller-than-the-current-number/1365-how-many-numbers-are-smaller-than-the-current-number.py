class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt=[0]*101
        for value in nums:
            cnt[value]+=1
        return [sum(cnt[:nums[i]]) for i in range(len(nums))]