class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index={}
        for i in range(len(nums)):
            index[nums[i]]=i
        for op in operations:
            nums[index[op[0]]]=op[1]
            index[op[1]]=index[op[0]]
        return nums
            
        
        