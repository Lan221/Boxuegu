n=int(input())
t = tuple(map(int,input().split()))
if len(t)!=n:
    print("please input correct number")
else:
    result = hash(t)
    print(result)