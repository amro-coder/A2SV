class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph=[[] for _ in range(n)]
        for node in range(n):
            for child in [leftChild[node],rightChild[node]]:
                if child !=-1:
                    graph[node].append(child)
                    graph[child].append(node)
        vis=[False]*n
        def dfs(node):
            vis[node]=True
            for child in graph[node]:
                if not vis[child]:
                    dfs(child)
        dfs(0)
        numParents=[0]*n
        for node in range(n):
            for child in [leftChild[node],rightChild[node]]:
                if child !=-1:
                    numParents[child]+=1
        return all(vis) and numParents.count(1)==n-1 and numParents.count(0)==1
        