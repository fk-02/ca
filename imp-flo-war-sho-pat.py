n=int(input())
m=int(input())
INF=10**15
d=[[INF]*n for _ in range(n)]
for i in range(n):d[i][i]=0
for _ in range(m):
 u,v,w=map(int,input().split())
 d[u-1][v-1]=min(d[u-1][v-1],w)
for k in range(n):
 for i in range(n):
  for j in range(n):
   if d[i][k]<INF and d[k][j]<INF:
    d[i][j]=min(d[i][j],d[i][k]+d[k][j])
for r in d:
 print(*[x if x<INF else "INF" for x in r],end=" \n")