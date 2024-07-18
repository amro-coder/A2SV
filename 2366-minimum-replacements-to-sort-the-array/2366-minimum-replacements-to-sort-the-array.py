class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        maxVal=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            numOp=(nums[i]-1)//maxVal
            ans+=numOp
            maxVal=nums[i]//(numOp+1)
        return ans
            
        