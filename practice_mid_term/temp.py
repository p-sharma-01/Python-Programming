s="4[a6[b]1[ab]]"
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
k=l[::-1]
for i in range(len(k)):
    p=s.rfind('[')
    q=s.find(']')
    w=s[p+1:q]*int(k[i])
    s=s[:s.index(k[i])]+w+s[q+1:]
print(s)