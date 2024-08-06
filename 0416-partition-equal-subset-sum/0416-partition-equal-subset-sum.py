class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.ans={}
        def solve(i,target):
            if target==0:
                self.ans[(i,target)]=True
            elif i>=len(nums) or target<0:
                self.ans[(i,target)]=False
            if (i,target) not in self.ans:
                self.ans[(i,target)]=(solve(i+1,target) or solve(i+1,target-nums[i]))
            return self.ans[(i,target)]
        solve(0,sum(nums)//2)
        return solve(0,sum(nums)//2) and (sum(nums)%2==0)