class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        prevBigger=[-1]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and nums[i]>nums[stack[-1]]:
                prevBigger[stack.pop()]=i
            stack.append(i)
        stack=[]
        for i in range(n):
            stack.append((nums[i],prevBigger[i]))
        stack.sort()
        for i in range(n):
            while stack and stack[-1][1]<=i:
                stack.pop()
            if stack and stack[-1][0]>nums[i]:
                return True
        return False
        