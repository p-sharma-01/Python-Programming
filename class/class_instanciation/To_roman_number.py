def to_roman(num):
  arr1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
  arr2=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
  
  roman_num=''
  i=0
  while num>0:
    for _ in range(num//arr1[i]):
      roman_num += arr2[i]
      num -= arr1[i]
    i+=1
  return roman_num
n = int(input())
print(to_roman(n))
      