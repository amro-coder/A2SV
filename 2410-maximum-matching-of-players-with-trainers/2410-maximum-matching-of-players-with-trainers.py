class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i,j,ans=len(players)-1,len(trainers)-1,0
        while i>=0 and j>=0:
            if players[i]<=trainers[j]:
                i,j,ans=i-1,j-1,ans+1
            else:
                i-=1
        return ans
        