class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[(nums[i],i) for i in range(len(nums))]
        x.sort()
        left_pointer,right_pointer=0,len(nums)-1
        while left_pointer<right_pointer:
            if x[left_pointer][0]+x[right_pointer][0]==target:
                return [x[left_pointer][1],x[right_pointer][1]]
            if  x[left_pointer][0]+x[right_pointer][0]<target:
                left_pointer+=1
            else:
                right_pointer-=1;
                