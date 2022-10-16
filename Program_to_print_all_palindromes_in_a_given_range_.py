x=int(input())
y=int(input())
s=0
for i in range(x,y+1):
    temp=i
    s=0
    while temp>0:
        d=temp%10
        temp=temp//10
        s=s*10+d
    if i==s:
        print(s,end=' ')