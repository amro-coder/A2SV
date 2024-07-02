class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n,current=len(num),[]
        def backtrack(index):
            if index==n:
                return len(current)>2                
            ans=False
            for i in range(index,n):
                temp=num[index:i+1]
                if (temp[0]!='0' or len(temp)==1) and (len(current)<2 or current[-1]+current[-2]==int(temp)):
                    current.append(int(temp))
                    ans|=backtrack(i+1)
                    current.pop()
                if ans: break
            return ans
        return backtrack(0)
                
