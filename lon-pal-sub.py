s=input();n=len(s)
d=[[0]*n for _ in range(n)]
for i in range(n):d[i][i]=1
for l in range(2,n+1):
 for i in range(n-l+1):
  j=i+l-1
  d[i][j]=2+(d[i+1][j-1]if l>2 else 0)if s[i]==s[j]else max(d[i+1][j],d[i][j-1])
print(d[0][n-1])