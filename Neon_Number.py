n=int(input())
sq=n*n
temp=n
sum=0
while sq:
    rem=sq%10
    sum=sum+rem
    sq=sq//10
if(sum==temp):
    print("Neon Number")
else:
    print("Not Neon Number")
