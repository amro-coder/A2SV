class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        maxVal=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=maxVal:
                maxVal=nums[i]
            elif nums[i]<=2*maxVal:
                ans+=1
                maxVal=nums[i]//2
            else:
                numOp=(nums[i]-1)//maxVal
                ans+=numOp
                maxVal=nums[i]//(numOp+1)

        return ans
            
        