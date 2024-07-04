class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree=[0]*n
        for u,v in edges:
            inDegree[v]+=1
        return [node for node in range(n) if inDegree[node]==0]
        