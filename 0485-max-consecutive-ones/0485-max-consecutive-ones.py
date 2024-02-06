class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zero_indexes=[-1]+[i for i in range(len(nums)) if nums[i]==0]+[len(nums)]
        ans=0
        for i in range(len(zero_indexes)-1):
            ans=max(ans,zero_indexes[i+1]-zero_indexes[i]-1)
        return ans