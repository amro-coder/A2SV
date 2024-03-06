class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left,right,ans=0,1,0
        while right<len(arr):
            while right<len(arr) and arr[right]>arr[right-1]:
                right+=1
            while right<len(arr) and right-left>1 and arr[right]<arr[right-1]:
                right+=1
                    
            if right-left>=3 and arr[right-1]<arr[right-2]:        
                ans=max(ans,right-left)
            
            left=max(left+1,right-1)
            right=left+1
            
        return ans
        
        