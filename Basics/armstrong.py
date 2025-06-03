n=int(input())
s=n
rb=0
while n:
    d=n%10
    rb+=d**len(str(s))
    n//=10
if s==rb:
    print("Armstrong Number")
else:
    print("not an armstrong Number")