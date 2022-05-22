a,b=map(int,input().split())
c=b
while True:
    if c%a==0 and c%b==0:
        print(c)
        break
    c+=1