class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        prefixSum=[0]+list(accumulate(nums))
        for i in range(n):
            dp[i][i]=nums[i]
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                dp[i][j]=max(nums[i]+ prefixSum[j+1]-prefixSum[i+1]-dp[i+1][j],nums[j]+prefixSum[j]-prefixSum[i]-dp[i][j-1])
        return 2*dp[0][n-1]>=sum(nums)
#         def getMaxScore(nums,ind=0):
#             if not nums:
#                 return [0,0]
#             op1=getMaxScore(nums[1:],1^ind)
#             op2=getMaxScore(nums[:-1],1^ind)
#             op1[ind]+=nums[0]
#             op2[ind]+=nums[-1]
#             return max(op1,op2,key=lambda a:a[ind])
                
#         player1,player2=getMaxScore(nums)
#         return player1>=player2