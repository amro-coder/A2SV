class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        ans=current_length=0
        cnt=defaultdict(int)
        last=word[0]
        for i in range(len(word)):
            if word[i]<last:
                cnt=defaultdict(int)
                current_length=0
                
            cnt[word[i]]+=1
            current_length+=1
            last=word[i]
            
            if min([cnt[c] for c in ['a','e','i','o','u']])>0:
                ans=max(ans,current_length)
                
        return ans
                
            