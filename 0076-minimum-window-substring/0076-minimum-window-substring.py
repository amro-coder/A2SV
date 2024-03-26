class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt,num_bad,j=defaultdict(int),len(set(t)),0
        target=Counter(t)
        best_range=[float("-inf"),float("inf")]
        for i in range(len(s)):
            while j<len(s) and num_bad>0:
                num_bad-=(cnt[s[j]]+1==target[s[j]])
                cnt[s[j]]+=1
                j+=1
            if num_bad==0:
                if j-i<best_range[1]-best_range[0]:
                    best_range=[i,j]
            num_bad+=(cnt[s[i]]==target[s[i]])
            cnt[s[i]]-=1

        return s[best_range[0]:best_range[1]] if best_range[0]!=float("-inf") else ""
                    
                
            
            
        