n=3
for i in range(1,n+1):
    for j in range(n-i+1):
        print(" ",end=" ")
    for j in range(i):
      print("*",end=" ")
    for j in range(1,i):
       print("*",end=" ")
    print()
for i in range(6):
  if i==1 or i==5:
      print("*",end=" ")
  else:
      print(" ",end=" ")
print()
for i in range(7):
  if i in [0,1,5,6]:
      print("*",end=" ")
  else:
    print("@",end=" ")
print()
for i in range(6):
  if i==1 or i==5:
      print("*",end=" ")
  else:
      print(" ",end=" ")

 