def gcd(a,b):
    if b==0:
        return a;
    return gcd(b,a%b)
n=int(input())
a=list(map(int,input().split()))
lcm=hcf=a[0]
for i in range(1,n):
    hcf=gcd(a[i],lcm)
    lcm=(a[i]*lcm)//hcf
print(lcm)
    