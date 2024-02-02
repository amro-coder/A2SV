class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        word1_pointer=0
        word2_pointer=0
        word1turn=True
        while(word1_pointer<len(word1) and word2_pointer<len(word2)):
            if (word1turn):
                ans+=word1[word1_pointer]
                word1_pointer+=1
                word1turn=False
            else:
                ans+=word2[word2_pointer]
                word2_pointer+=1
                word1turn=True
        ans+=word1[word1_pointer:]
        ans+=word2[word2_pointer:]
        return ans
            
        