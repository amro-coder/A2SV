class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            if (nums[i+1]<nums[i]):
                copy_nums=nums.copy()
                nums[i+1]=nums[i]
                copy_nums[i]=copy_nums[i+1]
                return sorted(nums)==nums or sorted(copy_nums)==copy_nums
        return True # there is only one element
            
        