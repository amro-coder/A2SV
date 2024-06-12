class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        cnt=[0]*(len(edges)*2+1)
        for u,v in edges:
            cnt[u],cnt[v]=cnt[u]+1,cnt[v]+1
        return cnt.index(max(cnt))