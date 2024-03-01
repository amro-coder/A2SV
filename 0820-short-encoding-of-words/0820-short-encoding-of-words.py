class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words=sorted(words,key=lambda a:len(a))
        ans=sum([len(i)+1 for i in words])
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][len(words[j])-len(words[i]):]:
                    ans-=len(words[i])+1
                    break
        return ans