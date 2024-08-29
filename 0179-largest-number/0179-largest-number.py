class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted([str(num) for num in nums], key=lambda x: x*10, reverse=True)) if set(nums)!=set([0]) else '0'
                
            
        