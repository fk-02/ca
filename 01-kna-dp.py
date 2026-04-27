n=int(input());c=int(input())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
d=[0]*(c+1)
for i in range(n):
    for j in range(c,w[i]-1,-1):
        d[j]=max(d[j],d[j-w[i]]+p[i])
print(d[c])