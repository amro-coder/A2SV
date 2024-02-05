# problem link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# solution:
if __name__ == '__main__':
    ans=[]
    all_scores=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_scores.add(score)
        ans.append((score,name))
    all_scores=sorted(all_scores)
    ans.sort()    
    for score,name in ans:
        if score==all_scores[1]:
            print(name)
        
