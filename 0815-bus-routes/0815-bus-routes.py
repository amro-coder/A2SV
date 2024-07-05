class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        numCities=max([max(i) for i in routes]+[source,target])+1
        n=numCities+len(routes)
        graph=[[] for _ in range(n)]
        for u in range(len(routes)):
            for v in routes[u]:
                graph[u+numCities].append(v)
                graph[v].append(u+numCities)
        dis=[-1]*n
        q=deque([source])
        dis[source]=0
        while q:
            parent=q.popleft()
            for child in graph[parent]:
                if dis[child]==-1:
                    dis[child]=dis[parent]+1
                    q.append(child)
        return -1 if dis[target]==-1 else dis[target]//2
        