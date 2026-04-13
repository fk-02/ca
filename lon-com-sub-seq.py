a,b,c=input(),input(),input()
d=[[[0]*(len(c)+1)for _ in range(len(b)+1)]for __ in range(len(a)+1)]
for i in range(1,len(a)+1):
 for j in range(1,len(b)+1):
  for k in range(1,len(c)+1):
   d[i][j][k]=1+d[i-1][j-1][k-1]if a[i-1]==b[j-1]==c[k-1]else max(d[i-1][j][k],d[i][j-1][k],d[i][j][k-1])
print(d[-1][-1][-1])