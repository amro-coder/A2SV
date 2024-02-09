class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        equal_pivot=0
        bigger_than_pivot=[]
        less_than_pivot=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                less_than_pivot.append(nums[i])
            elif nums[i]>pivot:
                bigger_than_pivot.append(nums[i])
            else:
                equal_pivot+=1
        return less_than_pivot+[pivot]*equal_pivot+bigger_than_pivot
        
        