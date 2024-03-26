class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeors,j,ans=0,0,0
        for i in range(len(nums)):
            while j<len(nums) and zeors+(nums[j]==0)<=1:
                zeors+=(nums[j]==0)
                j+=1
            ans=max(ans,j-i-zeors)
            zeors-=(nums[i]==0)
            
        return ans if nums.count(0)>0 else len(nums)-1
            
        