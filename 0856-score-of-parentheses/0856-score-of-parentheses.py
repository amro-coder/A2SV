class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                last=stack.pop()
                last=max(2*last,1)
                stack[-1]+=last
        return stack[-1]
                
                
            