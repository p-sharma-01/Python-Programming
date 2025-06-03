n=int(input())
a=0
b=1
s=a+b
for i in range(n):
    a=b
    b=s
    print(b,end=" ")
    s=a+b
