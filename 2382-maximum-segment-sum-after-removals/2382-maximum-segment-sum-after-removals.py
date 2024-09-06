class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n= len(nums)
        ans= [0 for i in range(n)]
        root= [i for i in range(n)]
        sz=[1 for i in range(n)]
        val= [0 for i in range(n)]
        def find(x):
            if x == root[x]:
                return x
            root[x]=find(root[x])
            return root[x]

        def union(x,y):
            rootX=find(x)
            rootY=find(y)
            if rootX != rootY:
                if sz[rootX]>sz[rootY]:
                    root[rootY] = rootX
                    sz[rootX] += sz[rootY]
                    ans[rootX]+=ans[rootY]
                else:
                    root[rootX] = rootY
                    sz[rootY] += sz[rootX]
                    ans[rootY]+=ans[rootX]
                
                    
        final_ans=[]
        removeQueries.reverse()
        current_ans=0
        for i in removeQueries:
            final_ans.append(current_ans)
            val[i] = nums[i]
            ans[i] += nums[i]
            if i+1 < n and val[i+1] >0:
                union(i,i+1)
            if i-1 >= 0 and val[i-1] >0:
                union(i,i-1)
            current_ans=max(current_ans,ans[find(i)])
        return reversed(final_ans)