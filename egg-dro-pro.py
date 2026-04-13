e=int(input());f=int(input())
m=0
while 1:
 m+=1;t=0;c=1
 for i in range(1,e+1):c=c*(m-i+1)//i;t+=c
 if t>=f:print(m);break