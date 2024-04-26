class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefixSum=[0]+list(accumulate(nums))
        q=deque()
        ans=float("inf")
        for i in range(len(prefixSum)):
            while q and prefixSum[i]-prefixSum[q[0]]>=k:
                ans=min(ans,i-q.popleft())
            while q and prefixSum[i]<=prefixSum[q[-1]]:
                q.pop()
            q.append(i)
        return ans if ans!=float("inf") else -1
                    