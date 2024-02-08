from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        num_loss=defaultdict(int)
        for match in matches:
            num_loss[match[1]]+=1;
            num_loss[match[0]]
        ans=[[],[]]
        for player in num_loss.keys():
            if num_loss[player]==0:
                ans[0].append(player)
            if num_loss[player]==1:
                ans[1].append(player)
        ans[0].sort()
        ans[1].sort()
        return ans