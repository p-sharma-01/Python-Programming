def validity(ls:list)->bool:
    if type(ls[0])==list:
        ln=len(ls[0])
        for i in ls:
            if len(i)!=ln or type(i)!=list:
                return False
            return True
    return False
        
r1,c1=list(map(int,input().split()))# 2 3
p=[]
temp=[]
k=list(map(int,input().split()))
for i in k:
    temp.append(i)
    if len(temp)==c1:
        p.append(temp)
        temp=[]
r2,c2=list(map(int,input().split()))
q=[]
temp2=[]
l=list(map(int,input().split()))
for i in l:
    temp2.append(i)
    if len(temp2)==c2:
        q.append(temp2)
        temp2=[]

if r1*c1==len(k) and r2*c2==len(l):
    if (r1,c1)==(r2,c2):
        if validity(p) and validity(q):
            w=[[0 for _ in range(c1)]for _ in range(r1)]
            for i in range(r1):
                for j in range(c1):
                    w[i][j]=p[i][j]+q[i][j]
            for i in w:
                print(*i)
        else:
            print("Invald matrix")
    else:
        print("Invalid matrix")
else:
    print("Invalid Matrix ")
            


