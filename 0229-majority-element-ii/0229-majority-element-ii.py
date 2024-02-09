from collections import Counter
class Solution:
    def majorityElement(self,nums):
        first_voted_value = None
        first_vote_cnt = 0
        second_voted_value = None
        second_vote_cnt = 0
        for i in range(len(nums)):
            if nums[i]==first_voted_value:
                first_vote_cnt+=1
            elif nums[i]==second_voted_value:
                second_vote_cnt+=1
            elif first_vote_cnt == 0:
                first_voted_value = nums[i]
                first_vote_cnt = 1
            elif second_vote_cnt==0:
                second_voted_value = nums[i]
                second_vote_cnt = 1
            else:
                first_vote_cnt-=1
                second_vote_cnt-=1

        first_vote_cnt = second_vote_cnt = 0
        for i in range(len(nums)):
            if nums[i] == first_voted_value:
                first_vote_cnt += 1
            if nums[i] == second_voted_value:
                second_vote_cnt += 1

        ans = []
        if first_vote_cnt > len(nums) // 3:
            ans.append(first_voted_value)
        if second_vote_cnt > len(nums) // 3:
            ans.append(second_voted_value)
        return ans
                
        
        
        
        