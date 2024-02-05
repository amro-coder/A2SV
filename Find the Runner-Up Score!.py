# problem link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# solution:
if __name__ == '__main__':
    n = int(input())
    arr = sorted(map(int, input().split()))
    for value in reversed(arr):
        if (value!=arr[-1]):
            print(value)
            break
