class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        num_zeros=0
        ans=[]
        for i in range(n):
            if nums[i] == 0:
                num_zeros+=1;
            else:
                ans.append(nums[i])
        return ans+[0]*num_zeros
        