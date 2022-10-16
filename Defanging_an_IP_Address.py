n=input()
d=[]
c="[.]"
for i in range(len(n)):
    if n[i]==".":
        d.append(c)
    else:
        d.append(n[i])
c="".join(d)
print(c)