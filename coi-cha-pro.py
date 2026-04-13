s=int(input())
n=int(input())
c=list(map(int,input().split()))
d=[1]+[0]*s
for x in c:
 for j in range(x,s+1):d[j]+=d[j-x]
print(d[s])