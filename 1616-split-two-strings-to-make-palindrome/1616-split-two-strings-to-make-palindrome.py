class Solution:
    def checkPalindromeFormation(self,a: str, b: str) -> bool:
        ans = a == a[::-1] or b == b[::-1]
        n=len(a)
        index = -1
        for i in range(n // 2):
            if a[i] != b[~i]:
                index = i
                break
        if index!=-1:
            s = a[index:n-index]
            ans |= s == s[::-1]
            s = b[index:n-index]
            ans |= s == s[::-1]
        else:
            ans=True

        index = -1
        for i in range(n // 2):
            if b[i] != a[~i]:
                index = i
                break
        if index!=-1:
            s = a[index:n-index]
            ans |= s == s[::-1]
            s = b[index:n-index]
            ans |= s == s[::-1]
            print(s)
        else:
            ans=True

        return ans
            
        
            
        