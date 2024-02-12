class Solution:
    def dis(self,start,end):
        return abs(start[0]-end[0]) + abs(start[1]-end[1])
    
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return all([self.dis(ghosts[i],target) > self.dis([0,0],target) for i in range(len(ghosts))])
        