n=int(input())
s=n
rb=0
while n:
    digit=n%10
    rb=rb*10+digit
    n=n//10
if s==rb:
    print("Palindrome")
else:
    print("Not a palindrome")