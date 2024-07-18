class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums.reverse()
        end,ans=0,0
        while end<n:
            if nums and nums[-1]<=end+1:
                end+=nums.pop()
            else:
                ans+=1
                end+=end+1
        return ans
                
                
        