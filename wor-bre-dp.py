n=int(input())
d=set(input().split())
s=input()
dp=[1]+[0]*len(s)
for i in range(1,len(s)+1):
 for j in range(i):
  if dp[j]and s[j:i]in d:dp[i]=1;break
print(dp[-1])