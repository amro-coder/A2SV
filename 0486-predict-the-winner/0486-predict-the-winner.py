class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def getMaxScore(nums,myturn=True):
            if not nums:
                return 0
            if myturn:
                return max(getMaxScore(nums[1:],False)+nums[0],getMaxScore(nums[:-1],False)+nums[-1])
            return min(getMaxScore(nums[1:],True),getMaxScore(nums[:-1],True))
        player1=getMaxScore(nums)
        player2=sum(nums)-player1
        return player1>=player2