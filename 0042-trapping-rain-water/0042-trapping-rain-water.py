class Solution:
    def trap(self, height: List[int]) -> int:
        max_right,left_max,ans=[0]*(len(height)+1),0,0
        for i in range(len(height)-1,-1,-1):
            max_right[i]=max(max_right[i+1],height[i])
        for i in range(len(height)):
            ans+=max(0,min(left_max,max_right[i+1])-height[i])
            left_max=max(left_max,height[i])
        return ans
            
        
        