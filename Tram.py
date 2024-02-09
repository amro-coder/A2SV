# problem link: https://codeforces.com/problemset/problem/116/A
# solution:
import sys
input=sys.stdin.readline
ans=-1
current_passangers=0
for _ in range(int(input())):
    exiting,entering=map(int,input().split())
    current_passangers-=exiting
    current_passangers+=entering
    ans=max(current_passangers,ans)
print(ans)
