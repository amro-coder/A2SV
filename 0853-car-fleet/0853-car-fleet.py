class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x=[]
        for i in range(len(position)):
            x.append((position[i],speed[i]))
        x.sort()
        ans=0
        thershold=-1
        for i in range(len(position)-1,-1,-1):
            t=(target-x[i][0])/x[i][1]
            ans+=t>thershold
            thershold=max(thershold,t)
        return ans
