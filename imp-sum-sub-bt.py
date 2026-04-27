n=int(input());a=list(map(int,input().split()));k=int(input());f=0
def s(i,t,p):
 global f
 if t==0:print(p);f=1;return
 if i==len(a)or t<0:return
 s(i+1,t,p)
 s(i+1,t-a[i],p+str(a[i])+" ")
s(0,k,"")
if not f:print(-1)