r1,c1=map(int,input().split())
p=[]
for i in range(r1):
    c=list(map(int,input().split()))
    p.append(c)
r2,c2=map(int,input().split())
q=[]
for i in range(r2):
    b=list(map(int,input().split()))
    q.append(b)
if c1==r2:
    w=[[0 for i in range(c2)] for j in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                w[i][j]+=p[i][k]*q[k][j]
    for i in w:
        print(*i)
else:
    print("Matrix multiplication doesn't supports dimensions")
