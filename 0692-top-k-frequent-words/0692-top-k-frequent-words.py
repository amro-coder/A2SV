class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt=Counter(words)
        h=[]
        for key,value in cnt.items():
            h.append((-value,key))
        heapify(h)
        ans=[]
        while k:
            _,s=heappop(h)
            ans.append(s)
            k-=1
        return ans
        
        