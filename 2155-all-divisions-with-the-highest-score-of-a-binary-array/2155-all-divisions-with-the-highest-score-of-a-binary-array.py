class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        max_score=current_score=nums.count(1)
        score=[(current_score,0)]
        for i in range(len(nums)):
            current_score+=(nums[i]==0)
            current_score-=(nums[i]==1)
            score.append((current_score,i+1))
            max_score=max(max_score,current_score)
        return [i[1] for i in score if i[0]==max_score]
    
        