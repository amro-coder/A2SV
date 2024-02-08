# problem link: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
# solution:
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        A.sort()
        B.sort()
        return A==B
