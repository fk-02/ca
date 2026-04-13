n=int(input())
f=list(map(int,input().split()))
p=[0]*n;p[0]=f[0]
for i in range(1,n):p[i]=p[i-1]+f[i]
g=lambda i,j:p[j]-(p[i-1] if i else 0)
d=[[0]*n for _ in range(n)]
for i in range(n):d[i][i]=f[i]
for l in range(2,n+1):
 for i in range(n-l+1):
  j=i+l-1;d[i][j]=10**9
  for r in range(i,j+1):
   d[i][j]=min(d[i][j],(d[i][r-1] if r>i else 0)+(d[r+1][j] if r<j else 0)+g(i,j))
for i in range(n):
 print(*([0]*i+[d[i][j]for j in range(i,n)]))