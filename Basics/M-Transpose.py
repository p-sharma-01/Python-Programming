r,c=map(int,input().split())
p=[]
for i in range(r):
    s=list(map(int,input().split()))
    p.append(s)
w=[[0 for i in range(r)]for j in range(c)]
for i in range(c):
    for j in range(r):
        w[i][j]=p[j][i]
for i in w:
    print(*i)

