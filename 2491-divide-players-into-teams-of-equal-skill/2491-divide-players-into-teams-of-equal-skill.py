class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target=skill[0]+skill[-1]
        ans=0
        for i in range(len(skill)//2):
            if skill[i]+skill[~i]!=target:
                ans=-1
                break
            ans+=skill[i]*skill[~i]
        return ans
        