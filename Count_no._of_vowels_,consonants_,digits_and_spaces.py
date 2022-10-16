n=input()
v="aeiouAEIOU"
vc=0
cc=0
dc=0
sc=0
for i in n:
    if i in v:
        vc+=1
    elif i.isalpha():
        cc+=1
    elif i.isdigit():
        dc+=1
    elif ord(i)==32:
        sc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",dc)
print("White spaces:",sc)