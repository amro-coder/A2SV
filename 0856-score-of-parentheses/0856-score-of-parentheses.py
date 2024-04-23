class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=0
        stack=[]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                last=stack.pop()
                if last==0:
                    last+=1
                else:
                    last*=2
                if not stack:
                    ans+=last
                else:
                    stack[-1]+=last
        return ans
                
                
            