class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        visited=[False]*(n+1)
        for value in nums:
            visited[value]=True
        for value in range(n+1):
            if (not visited[value]):
                return value
        