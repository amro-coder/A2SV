class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_occupied=0
        for i in range(1,len(nums)):
            if nums[last_occupied]!=nums[i]:
                nums[last_occupied+1],nums[i]=nums[i],nums[last_occupied+1]
                last_occupied+=1
        return last_occupied+1