# problem link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# solution:
if __name__ == '__main__':
    ans=[]
    n = int(input())
    for _ in range(n):
        command=input().split()
        if command[0]=="insert":
            ans.insert(int(command[1]),int(command[2]))
        if command[0]=="print":
            print(ans)        
        if command[0]=="remove":
            ans.remove(int(command[1]))
        if command[0]=="append":
            ans.append(int(command[1]))
        if command[0]=="sort":
            ans.sort()
        if command[0]=="pop":
            ans.pop()
        if command[0]=="reverse":
            ans.reverse()
            
        
        

            
