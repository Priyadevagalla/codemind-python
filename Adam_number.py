x=int(input())
k=x*x
z=0
s=0
while x:
    d=x%10
    x=x//10
    z=z*10+d
h=z*z
while h:
    d=h%10
    h=h//10
    s=s*10+d
if s==k:
    print("True")
else:
    print("False")