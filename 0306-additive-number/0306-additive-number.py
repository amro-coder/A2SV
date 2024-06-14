class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        for i in range(1,n):
            for j in range(i,n):
                if j-i<1 or (num[0]=='0' and i>1) or (num[i]=='0' and j-i>1):
                    continue
                num1=int(num[:i])
                num2=int(num[i:j])
                num3=num1+num2
                mynum=num[:j]
                while len(mynum)<len(num):
                    mynum+=str(num3)
                    num1,num2=num2,num3
                    num3=num1+num2
                if mynum==num:
                    return True
        return False
