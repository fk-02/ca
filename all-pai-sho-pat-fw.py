n=int(input());I=10**15
d=[list(map(int,input().split()))for _ in range(n)]
for i in range(n):
 for j in range(n):
  if d[i][j]==-1 and i!=j:d[i][j]=I
for k in range(n):
 for i in range(n):
  for j in range(n):
   if d[i][k]<I and d[k][j]<I:d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for r in d:print(*[x if x<I else"INF"for x in r],end=" \n")