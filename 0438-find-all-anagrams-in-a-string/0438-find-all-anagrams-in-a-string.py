class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans,target_cnt,cnt=[],Counter(p),Counter(s[:min(len(p),len(s))])
        if target_cnt==cnt:
            ans.append(0)
        for i in range(len(p),len(s)):
            cnt[s[i]]+=1
            cnt[s[i-len(p)]]-=1
            if cnt[s[i-len(p)]]==0:
                del cnt[s[i-len(p)]]
            
            if target_cnt==cnt:
                ans.append(i-len(p)+1)
                
        return ans
                
        
        
        
            
        