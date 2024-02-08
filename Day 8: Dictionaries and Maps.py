# problem link:https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# solution:
n=int(input())
phone_book={}
for _ in range(n):
    name,num=input().strip().split()
    phone_book[name]=num
while True:
    try:
        query_name = input().strip()
        try:
            print(f"{query_name}={phone_book[query_name]}")
        except:
            print("Not found")
    except:
        break
