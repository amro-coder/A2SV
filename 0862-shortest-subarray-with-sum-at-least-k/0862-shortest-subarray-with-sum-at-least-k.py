class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum=[0]+list(accumulate(nums))
        stack=[]
        ans=float("inf")
        for i in range(len(prefixSum)):
            low,high=0,len(stack)-1
            while low<=high:
                mid=(low+high)>>1
                if prefixSum[i]-prefixSum[stack[mid]]<k:
                    high=mid-1
                else:
                    low=mid+1
            if high>-1:
                ans=min(ans,i-stack[high])
                    
            while stack and prefixSum[i]<=prefixSum[stack[-1]]:
                stack.pop()
            stack.append(i)
        return ans if ans!=float("inf") else -1
                    