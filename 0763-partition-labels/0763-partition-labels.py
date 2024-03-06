class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_index=[-1]*26
        for i in range(len(s)):
            last_index[ord(s[i])-97]=i
            
        ans=[]
        current_size,have_to_reach=0,0
        for i in range(len(s)):
            have_to_reach=max(have_to_reach,last_index[ord(s[i])-97])
            current_size+=1
            if have_to_reach==i:
                ans.append(current_size)
                current_size,have_to_reach=0,0
                
        return ans
                
            
            