class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        for index in range(min([len(strs[j]) for j in range(len(strs))])):
            if all(strs[j][index]==strs[0][index] for j in range(len(strs))):
                ans+=strs[0][index]
            else:
                break
        return ans
        