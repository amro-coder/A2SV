class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt,ans,left,right=defaultdict(int),0,0,0
        while right<len(s):
            if cnt[s[right]]>0:
                cnt[s[left]]-=1
                left+=1
            else:
                cnt[s[right]]+=1
                right+=1
            ans= max(ans,right-left)

        return max(ans,right-left)
                
                
        