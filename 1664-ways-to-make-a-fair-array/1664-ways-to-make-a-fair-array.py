class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd,even,n=[0],[0],len(nums)
        for i in range(n):
            odd.append(odd[-1]+(nums[i] if i&1 else 0))
            even.append(even[-1]+(nums[i] if not(i&1) else 0))
        ans=0
        for i in range(n):
            ans+= ((even[i]+odd[n]-odd[i+1])==(odd[i]+even[n]-even[i+1]))
        return ans
        