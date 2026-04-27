n=int(input())
g=[list(map(int,input().split()))for _ in range(n)]
p=[0];v=[0]*n;v[0]=1;f=0
def dfs(u):
 global f
 if f:return
 if len(p)==n:
  if g[p[-1]][p[0]]:
   print(*p,p[0]);f=1
  return
 for i in range(n):
  if g[u][i]and not v[i]:
   v[i]=1;p.append(i)
   dfs(i)
   p.pop();v[i]=0
dfs(0)
if not f:print("Solution does not exist")