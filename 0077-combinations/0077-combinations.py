class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        current=[]
        def comb(start,end,k):
            if k==0:
                ans.append(current.copy())
                return
            if end<start:
                return
            comb(start+1,end,k)
            current.append(start)
            comb(start+1,end,k-1)
            current.pop()
            return
        comb(1,n,k)
        return ans
                
        