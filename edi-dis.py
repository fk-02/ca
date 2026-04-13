a,b=input(),input()
p=list(range(len(b)+1))
for i,x in enumerate(a,1):
 c=[i]+[0]*len(b)
 for j,y in enumerate(b,1):
  c[j]=p[j-1]if x==y else 1+min(p[j],c[j-1],p[j-1])
 p=c
print(p[-1])