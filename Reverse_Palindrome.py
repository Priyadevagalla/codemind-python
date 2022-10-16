def pal(a):
    r=t=0
    while a:
        r=a%10
        t=(t*10)+r
        a=a//10
    return t
n=int(input())
k=n
k=k+pal(k)
while 1:
    if k==pal(k):
        print(k)
        break
    else:
        k=k+pal(k)