class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find_parent(x):
            node=x
            while(x!=parent[x]):
                x=parent[x]
            while node!=x: node,parent[node]=parent[node],x
            return x

        def unite(x,y):
            parent_x,parent_y=find_parent(x),find_parent(y)
            if parent_x!=parent_y:
                if size[parent_x]<size[parent_y]:
                    parent_x,parent_y=parent_y,parent_x
                size[parent_x]+=size[parent_y]
                parent[parent_y]=parent_x
                return True
            return False
        
        n=max([max(i) for i in edges])
        parent=[i for i in range(n)]
        size=[1]*n
        for u,v in edges:
            if not unite(u-1,v-1):
                return (u,v)
        