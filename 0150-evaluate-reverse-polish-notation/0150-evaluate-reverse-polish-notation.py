class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]
        for t in tokens:
            if t.lstrip("-").isnumeric():
                ans.append(int(t))
            else:
                num2=ans.pop()
                num1=ans.pop()
                if t=="+":
                    ans.append(num1+num2)
                elif t=="-":
                    ans.append(num1-num2)
                elif t=="*":
                    ans.append(num1*num2)
                else:
                    ans.append(int(num1/num2))
        return ans[0]
        