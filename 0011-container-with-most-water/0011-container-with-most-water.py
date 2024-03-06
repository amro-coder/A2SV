class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,ans=0,len(height)-1,0
        while left<right:
            ans=max(ans,min(height[left],height[right])*(right-left))
            if height[left]==height[right]:
                left+=1
                right-=1
            elif height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
                
        