n=int(input());p=list(map(int,input().split()))
d=[[0]*n for _ in range(n)]
for l in range(2,n):
 for i in range(1,n-l+1):
  j=i+l-1;d[i][j]=10**18
  for k in range(i,j):d[i][j]=min(d[i][j],d[i][k]+d[k+1][j]+p[i-1]*p[k]*p[j])
print(d[1][n-1])