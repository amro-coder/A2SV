class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        cnt,j,ans=0,-1,0
        for i in range(len(answerKey)):
            while j+1<len(answerKey) and (cnt + (answerKey[j+1]=="F"))<=k:
                cnt += (answerKey[j+1]=="F")
                j+=1
            ans=max(ans,j-i+1)
            cnt -= answerKey[i]=="F"
            
        cnt,j=0,-1
        for i in range(len(answerKey)):
            while j+1<len(answerKey) and (cnt + (answerKey[j+1]=="T"))<=k:
                cnt += (answerKey[j+1]=="T")
                j+=1
            ans=max(ans,j-i+1)
            cnt -= answerKey[i]=="T"
        
            
        return ans
                
        