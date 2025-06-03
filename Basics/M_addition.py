def validity(lst):
    if type(lst[0])==list:
        ln=len(lst[0])
        for i in lst:
            if type(i)!=list or len(i)!=ln:
                return False
            return True
    return False
r1,c1=map(int,input().split())
p=[]
for i in range(r1):
    k=list(map(int,input().split()))
    p.append(k)
r2,c2=map(int,input().split())
q=[]
for i in range(r2):
    l=list(map(int,input().split()))
    q.append(l)
if validity(p) and validity(q):
    if [r1,c1]==[r2,c2]:
        w=[[0 for i in range(c1)] for j in range(r1)]
        for i in range(r1):
            for j in range(c1):
                w[i][j]+=p[i][j]+q[i][j]
        for i in w:
            print(*i)
    else:
        print("Matrices dimensions are not acceptable for addition")
else:
    print("Matrices are not valid")