class Solution:
    def largestNumber(self, num: List[int]) -> str:
        def custom_compare(x,y):
            s1=''.join([str(i) for i in x])
            s2=''.join([str(i) for i in y])
            return s1>s2
        n=len(num)
        dp=[[] for _ in range(n)]
        dp[-1].append(num[-1])
        for i in range(n-2,-1,-1):
            best_ans=dp[i+1].copy()
            best_ans.append(num[i])
            for j in range(len(dp[i+1])):
                temp=dp[i+1].copy()
                temp.insert(j,num[i])
                if custom_compare(temp,best_ans):
                    best_ans=temp
            dp[i]=best_ans
        ans=''.join([str(i) for i in dp[0]])
        for i in range(len(ans)):
            if ans[i]!='0':
                return ans[i:]
        return "0"
    
                
            
        