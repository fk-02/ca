n=int(input())
a=list(map(int,input().split()))
k=(n+1)//2
s=sum(a)
best=(10**18,10**18,[])
def f(i,c,x,y):
    global best
    if c==k:
        best=min(best,(abs(2*x-s),x,y[:]))
        return
    if i<n:
        f(i+1,c+1,x+a[i],y+[i])
        f(i+1,c,x,y)
f(0,0,0,[])
idx=set(best[2])
A=[a[i] for i in range(n) if i in idx]
B=[a[i] for i in range(n) if i not in idx]
if sum(A)<=sum(B):
    print(*A, end=" \n")
    print(*B, end=" ")
else:
    print(*B, end=" \n")
    print(*A, end=" ")