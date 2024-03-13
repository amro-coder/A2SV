class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        current_min,current_max=0,0
        for i in range(len(nums)-indexDifference):
            if nums[i]>nums[current_max]:
                current_max=i
            if nums[i]<nums[current_min]:
                current_min=i
            if nums[current_max]-nums[indexDifference+i]>=valueDifference:
                return [current_max,indexDifference+i]
            if nums[indexDifference+i]-nums[current_min]>=valueDifference:
                return [current_min,indexDifference+i]
        return [-1,-1]
                
                
        
                
                
        