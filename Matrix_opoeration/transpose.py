a=[[1,2,4],[5,6,7]]
for i in a:
    print(*i)
r1,c1=len(a),len(a[0])
w=[[0 for _ in range(r1)] for _ in range(c1)]
for i in range(c1):
    for j in range(r1):
        w[i][j]=a[j][i]
for i in w:
    print(*i)
        