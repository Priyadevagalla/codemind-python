n=int(input())
x=list(map(int,input().split()))
c=d=0
for i in x:
    c=0
    for j in x:
        if j%i!=0:
            c=1
            break
    if c==0:
        print(i)
        d=1
        break
if d==0:
    print("1")