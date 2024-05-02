class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def getMaxScore(nums,myturn=True):
            if not nums:
                return (0,0)
            if myturn:
                op1=getMaxScore(nums[1:],False)
                op1=(op1[0]+nums[0],op1[1])
                op2=getMaxScore(nums[:-1],False)
                op2=(op2[0]+nums[-1],op2[1])
                return max(op1,op2)
                
            else:
                op1=getMaxScore(nums[1:],True)
                op1=(op1[0],op1[1]+nums[0])
                op2=getMaxScore(nums[:-1],True)
                op2=(op2[0],op2[1]+nums[-1])
                return min(op1,op2)
                
        player1,player2=getMaxScore(nums)
        return player1>=player2