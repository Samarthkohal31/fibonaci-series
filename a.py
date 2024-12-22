n=int(input("enter the number"))
a=0
b=1
c=0

print(a)
print(b)
while n>0:
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)