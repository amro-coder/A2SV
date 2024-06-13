class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for u,v in trust:
            graph[u-1].append(v-1)
        ans=graph.index(min(graph,key= lambda a:len(a)))
        graph[ans].append(ans)
        return ans+1 if all([ans in i for i in graph]) and len(graph[ans])==1 else -1
        