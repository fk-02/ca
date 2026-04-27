L=int(input());n=int(input())
a=[0]+sorted(map(int,input().split()))+[L]
from functools import lru_cache
@lru_cache(None)
def f(i,j):
    if j-i==1:return (0,())
    x=(10**18,())
    for k in range(i+1,j):
        c,p=f(i,k);d,q=f(k,j)
        t=(c+d+a[j]-a[i],(a[k],)+p+q)
        if t<x:x=t
    return x
print(*f(0,n+1)[1], end=" ")