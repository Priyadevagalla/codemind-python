s=input().split()
s=sorted(s)
s.sort(key=len)
print(*s)