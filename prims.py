V=int(input())
g=[list(map(int,input().split()))for _ in range(V)]
p=[-1]*V;k=[10**9]*V;m=[0]*V;k[0]=0
for _ in range(V-1):
 u=min((k[i],i)for i in range(V)if not m[i])[1]
 m[u]=1
 for v in range(V):
  if g[u][v]and not m[v]and g[u][v]<k[v]:k[v]=g[u][v];p[v]=u
print("Edge -> Weight")
for i in range(1,V):print(f"{p[i]} - {i} -> {g[i][p[i]]} ")