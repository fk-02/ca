n=int(input())
p=list(map(int,input().split()))
b1=b2=-10**9;s1=s2=0
for x in p:b1=max(b1,-x);s1=max(s1,b1+x);b2=max(b2,s1-x);s2=max(s2,b2+x)
print(s2)