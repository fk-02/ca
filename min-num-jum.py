n=int(input());a=list(map(int,input().split()))
if n<2:print(0)
elif a[0]==0:print(-1)
else:
 m=s=a[0];j=1
 for i in range(1,n):
  if i==n-1:print(j);break
  m=max(m,i+a[i]);s-=1
  if s==0:
   j+=1
   if i>=m:print(-1);break
   s=m-i
 else:print(-1)