x=int(input())
c=0
k=0
while x:
    z=int(input())
    k=0
    temp=z
    while z:
        d=z%10
        z=z//10
        k=k*10+d
    if(k==temp):
        print('True')
    else:
        print('False')
    
