class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        qMin,qMax,ans,start=deque(),deque(),1,0
        for i in range(n):
            while qMin and nums[i]<=qMin[-1][0]:
                qMin.pop()
            qMin.append((nums[i],i))
            
            while qMax and nums[i]>=qMax[-1][0]:
                qMax.pop()
            qMax.append((nums[i],i))
            
            while qMin and qMax and qMax[0][0]-qMin[0][0]>limit:
                start+=1
                if qMin[0][1]<start:
                    qMin.popleft()
                if qMax[0][1]<start:
                    qMax.popleft()
            
            ans=max(ans,i-start+1)
        return ans