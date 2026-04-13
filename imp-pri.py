n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
v=[0]*n;h=[(0,0)];r=0
import heapq
while h:
 w,u=heapq.heappop(h)
 if v[u]:continue
 v[u]=1;r+=w
 for i,x in enumerate(a[u]):
  if x and not v[i]:heapq.heappush(h,(x,i))
print(r)