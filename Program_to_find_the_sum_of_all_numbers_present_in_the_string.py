x=input()
sum=0
for i in x:
    if i.isdigit():
        sum=sum+int(i)
print(sum)