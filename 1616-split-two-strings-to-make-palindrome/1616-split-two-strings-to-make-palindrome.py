class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        ans= a==a[::-1] or b==b[::-1]
        
        start=len(a)//2-1
        end=start+1+(len(a)&1)
        a_is_palindrom=[True]+[False]*(len(a)//2-1)
        for i in range(1,len(a)//2):
            if a[start]==a[end]:
                a_is_palindrom[i]=True
            else:
                break
            start-=1
            end+=1
                
        b_is_palindrom=[True]+[False]*(len(b)//2-1)
        start=len(b)//2-1
        end=start+1+(len(b)&1)
        for i in range(1,len(b)//2):
            if b[start]==b[end]:
                b_is_palindrom[i]=True
            else:
                break
            start-=1
            end+=1
                
        for i in range(len(a)//2):
            if a[i]!=b[~i]:
                break
            ans|=b_is_palindrom[~i]|a_is_palindrom[~i]
        
        for i in range(len(b)//2):
            if b[i]!=a[~i]:
                break
            ans|=b_is_palindrom[~i]|a_is_palindrom[~i]
                
        return ans
        
            
        