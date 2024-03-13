class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        current_min,current_max,ans=0,0,[-1,-1]
        for i in range(len(nums)-indexDifference):
            if nums[i]>nums[current_max]:
                current_max=i
            if nums[i]<nums[current_min]:
                current_min=i
            if nums[current_max]-nums[indexDifference+i]>=valueDifference:
                ans=[current_max,indexDifference+i]
            if nums[indexDifference+i]-nums[current_min]>=valueDifference:
                ans=[current_min,indexDifference+i]
        return ans
                
                
        
                
                
        