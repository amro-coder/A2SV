class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans=0
        for val in arr:
            if val>ans:
                ans+=1
        return ans
        