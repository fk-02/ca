n=int(input())
if n==1:
 print([1])
elif n<4:
 for _ in range(n):print([0]*n)
else:
 b=[[0]*n for _ in range(n)]
 def f(r):
  if r==n:return 1
  for c in range(n):
   if all(b[i][c]==0 for i in range(r))and all(b[r-i-1][c-i-1]==0 for i in range(min(r,c)))and all(b[r-i-1][c+i+1]==0 for i in range(min(r,n-c-1))):
    b[r][c]=1
    if f(r+1):return 1
    b[r][c]=0
  return 0
 f(0)
 for r in b:print(r)