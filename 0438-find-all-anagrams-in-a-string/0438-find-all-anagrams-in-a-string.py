class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt, cnt_false, target_cnt, ans = defaultdict(int), 0, defaultdict(int), []
        for value in p:
            target_cnt[value] += 1
        for i in range(min(len(p), len(s))):
            cnt[s[i]] += 1
        for key in set(list(target_cnt.keys())+list(cnt.keys())):
            cnt_false += target_cnt[key] != cnt[key]
        if cnt_false == 0:
            ans.append(0)
        for i in range(len(p), len(s)):
            cnt_false += (cnt[s[i - len(p)]] == target_cnt[s[i - len(p)]]) - (cnt[s[i - len(p)]] == target_cnt[s[i - len(p)]] + 1)
            cnt[s[i - len(p)]] -= 1

            cnt_false += (cnt[s[i]] == target_cnt[s[i]]) - (cnt[s[i]] == target_cnt[s[i]] - 1)
            cnt[s[i]] += 1

            if cnt_false == 0:
                ans.append(i - len(p) + 1)
        return ans
            
        
        
            
        