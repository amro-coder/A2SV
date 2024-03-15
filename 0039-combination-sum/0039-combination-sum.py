class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[[]]
        for value in candidates:
            temp=deepcopy(ans)
            for comb in temp:
                for i in range(1,21):
                    if sum(comb)+i*value<=target:
                        ans.append(comb+[value]*i)
        final_ans=[i for i in ans if sum(i)==target]
        return final_ans
                
                
        