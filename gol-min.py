n,m=map(int,input().split())
a=list(map(int,input().split()))
g=[a[i*m:(i+1)*m] for i in range(n)]
for j in range(m-2,-1,-1):
 for i in range(n):
  g[i][j]+=max(
   g[i][j+1],
   g[i-1][j+1] if i else 0,
   g[i+1][j+1] if i<n-1 else 0
  )
print(max(r[0]for r in g))