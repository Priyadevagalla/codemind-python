s=input()
n=[]
for i in s:
    if i.isdigit() and i not in n:
        n.append(i)
n.sort()
d=0
for i in range(len(n)):
    if int(n[i])%2==0:
        t=n[i]
        n[i]=n[0]
        n[0]=t
        d=1
        break
kk="".join(n)
if d==1:
    print(kk[::-1])
else:
    print("-1")