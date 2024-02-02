from collections import Counter,defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter=defaultdict(int,Counter(s))
        t_counter=defaultdict(int,Counter(t))
        for letter in list(s_counter.keys())+list(t_counter.keys()):
            if s_counter[letter]<t_counter[letter]:
                return letter
