class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s,new_t=[],[]
        hashtag_cnt=0
        for i in range(len(s)-1,-1,-1):
            if hashtag_cnt==0 and s[i]!="#":
                new_s.append(s[i])
            else:
                hashtag_cnt+= s[i]=="#"
                hashtag_cnt-= s[i]!="#"
            
        hashtag_cnt=0
        for i in range(len(t)-1,-1,-1):
            if hashtag_cnt==0 and t[i]!="#":
                new_t.append(t[i])
            else:
                hashtag_cnt+= t[i]=="#"
                hashtag_cnt-= t[i]!="#"

            
        return new_s==new_t
        
            