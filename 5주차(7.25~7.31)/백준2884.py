a,b=input().split()
a=int(a)
b=int(b)
if b<45:
    if a==0:
        a=23
        b=60+b-45
    elif a!=0:
        a-=1
        b=b+60-45
elif b>=45:
    b-=45
    
print(a,b)