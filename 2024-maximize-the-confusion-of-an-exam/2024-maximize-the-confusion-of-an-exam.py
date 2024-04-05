class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        cnt1,j1,cnt2,j2,ans=0,-1,0,-1,0
        for i in range(len(answerKey)):
            while j1+1<len(answerKey) and (cnt1 + (answerKey[j1+1]=="F"))<=k:
                cnt1 += (answerKey[j1+1]=="F")
                j1+=1
            while j2+1<len(answerKey) and (cnt2 + (answerKey[j2+1]=="T"))<=k:
                cnt2 += (answerKey[j2+1]=="T")
                j2+=1
            ans=max(ans,max(j1,j2)-i+1)
            cnt1 -= answerKey[i]=="F"
            cnt2 -= answerKey[i]=="T"
                
            
        return ans
                
        