class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if 0 in nums:
            first_zero=nums.index(0)
            i=first_zero+1
            while i<len(nums):
                if nums[i]!=0:
                    nums[i],nums[first_zero]=nums[first_zero],nums[i]
                    first_zero+=1
                i+=1
                    
        