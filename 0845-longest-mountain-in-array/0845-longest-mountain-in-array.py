class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left,right,ans=0,1,0
        while right<len(arr):
            cnt1=0 # how many > condition is satisfied
            cnt2=0 # how many < condition is satisfied
            while right<len(arr) and arr[right]>arr[right-1]:
                cnt1+=1
                right+=1
            if cnt1>0:
                while right<len(arr) and arr[right]<arr[right-1]:
                    cnt2+=1
                    right+=1
                    
            if cnt1>0 and cnt2>0:        
                ans=max(ans,right-left)
            
            left=max(left+1,right-1)
            right=left+1
            
        return ans if ans>2 else 0
        
        