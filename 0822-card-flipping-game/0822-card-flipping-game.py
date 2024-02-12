class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cant_be_good=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                cant_be_good.add(fronts[i])
        ans=2000 + 1
        for value in fronts+backs:
            if value not in cant_be_good:
                ans=min(ans,value)
        return ans if ans!=2000+1 else 0