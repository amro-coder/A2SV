class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        suffix_sum=list(accumulate(shifts[::-1]))[::-1]
        return ''.join([chr(97+(ord(s[i])-97+suffix_sum[i])%26) for i in range(len(s))])
        