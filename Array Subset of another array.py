# problem link:https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
# solution:
from collections import Counter,defaultdict
def isSubset( a1, a2, n, m):
    count_a1=defaultdict(int,Counter(a1))
    count_a2=defaultdict(int,Counter(a2))
    for value in count_a2.keys():
        if count_a2[value]>count_a1[value]:
            return "No"
    return "Yes"
