n,k=map(int,input().split());m=10**9+7
if n<2:print(k%m)
else:
 s,d=0,k
 for _ in range(2,n+1):s,d=d%m,(s+d)*(k-1)%m
 print((s+d)%m)