class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack,biggestValidNum=[],float("-inf")
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<biggestValidNum:
                return True
            while stack and nums[i]>stack[-1]:
                biggestValidNum=stack.pop()
            stack.append(nums[i])
        return False
        