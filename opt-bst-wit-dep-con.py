n,D=map(int,input().split())
k=list(map(int,input().split()))
f=list(map(int,input().split()))
p=[[0]*n for _ in range(n)]
for i in range(n):
 p[i][i]=f[i]
 for j in range(i+1,n):p[i][j]=p[i][j-1]+f[j]
from functools import lru_cache as c
@c(None)
def s(i,j,d):
 if i>j:return 0
 if d>D:return 10**18
 return min((s(i,r-1,d+1)+s(r+1,j,d+1)+p[i][j] for r in range(i,j+1)),default=10**18)
r=s(0,n-1,1)
print(-1 if r>=10**18 else r)