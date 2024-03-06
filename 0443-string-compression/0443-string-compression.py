class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j=0,0
        while j<len(chars):
            cnt,letter=0,chars[j]
            while j<len(chars) and chars[j]==letter:
                cnt+=1
                j+=1
            to_put=[letter]
            if cnt>1:
                to_put+=list(str(cnt))
            for k in range(len(to_put)):
                chars[i]=to_put[k]
                i+=1
        return i
            
            
            
        