class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nxt,stack=[n]*n,[]
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                nxt[stack.pop()]=i
            stack.append(i)
        prev,stack=[-1]*n,[]
        for i in range(n-1,-1,-1):
            while stack and heights[i]<heights[stack[-1]]:
                prev[stack.pop()]=i
            stack.append(i)
        ans=0
        for i in range(n):
            ans=max(ans,(nxt[i]-prev[i]-1)*heights[i])
        return ans
        