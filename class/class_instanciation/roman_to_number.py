def to_num(s):
  d = {'I':1 , 'V': 5, 'X': 10 , 'L': 50, 'C':100 , 'D': 500, 'M':1000}
  total = 0
  prev_val=0
  for i in reversed(s):
    value = d[i]
    if value < prev_val:
      total -= value
    else:
      total += value
    prev_val = value
  return total
n = input()
print(to_num(n))