class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def getAns(n,k,start):
            if n==1:
                return start
            if k<=(1<<(n-2)):
                return getAns(n-1,k,start)
            return getAns(n-1,k-(1<<(n-2)),1^start)
        return getAns(n,k,0)
                    
            
                
        