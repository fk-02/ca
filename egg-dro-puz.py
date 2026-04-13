e,f=map(int,input().split())
dp=[[0]*(f+1) for _ in range(e+1)]
for i in range(1,e+1):
    dp[i][1]=1
for j in range(f+1):
    dp[1][j]=j
for i in range(2,e+1):
    for j in range(2,f+1):
        dp[i][j]=min(1+max(dp[i-1][x-1],dp[i][j-x]) for x in range(1,j+1))
print(dp[e][f])