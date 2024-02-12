class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        thrid_row="zxcvbnm"
        ans=[]
        for word in words:
            rows_needed=[]
            for letter in word:
                if letter.lower() in first_row:
                    rows_needed.append(1)
                if letter.lower() in second_row:
                    rows_needed.append(2)
                if letter.lower() in thrid_row:
                    rows_needed.append(3)
            if len(set(rows_needed))==1:
                ans.append(word)
        return ans
        