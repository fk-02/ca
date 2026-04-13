n=int(input());r=[];b=[0]*n
def f(c):
 if c==n:r.append(b[:]);return
 for i in range(n):
  if all(b[j]!=i and abs(b[j]-i)!=abs(j-c)for j in range(c)):
   b[c]=i;f(c+1)
f(0)
print(-1 if not r else"\n".join(" ".join(map(str,s))for s in r))