x=int(input())
c=0
k=0
while x:
    d=x%10
    x=x//10
    k=k*10+d
    c+=1
if c==10:
    d=k%10
    if(d==0):
        print("invalid")
    else:
        print("Valid")
else:
        print("Invalid")