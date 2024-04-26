class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n,limit=len(nums),2
        qMin,qMax,ans,start=deque(),deque(),0,0
        for i in range(n):
            while qMin and nums[i]<=qMin[-1][0]:
                qMin.pop()
            qMin.append((nums[i],i))
            
            while qMax and nums[i]>=qMax[-1][0]:
                qMax.pop()
            qMax.append((nums[i],i))
            
            while qMin and qMax and qMax[0][0]-qMin[0][0]>limit:
                ans+=i-start
                start+=1
                if qMin[0][1]<start:
                    qMin.popleft()
                if qMax[0][1]<start:
                    qMax.popleft()
                    
        for i in range(start,n):
            ans+=n-i
            
        return ans