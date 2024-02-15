class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans=defaultdict(int)
        for conunt_paired_domain in cpdomains:
            num,website=conunt_paired_domain.split()
            num=int(num)
            ans[website]+=num
            for i in range(len(website)):
                if website[i]=='.':
                    ans[website[i+1:]]+=num
        return [str(num) + " " + website for website,num in ans.items()]
            
                
                
        