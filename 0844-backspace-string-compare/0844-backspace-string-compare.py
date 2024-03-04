class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s,t=list(s),list(t)
        while '#' in s:
            index=s.index('#')
            if index!=0:
                s[index-1:index+1]=[]
            else:
                s.pop(index)
        while '#' in t:
            index=t.index('#')
            if index!=0:
                t[index-1:index+1]=[]
            else:
                t.pop(index)
        return s==t