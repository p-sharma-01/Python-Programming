def validity(ls:list)->bool:
    lt=ls[0]
    llt=len(lt)
    if(type(lt)==list):
        for i in ls:
            if(type(i)!= list or len(i)!= llt):
                return False
            return True
    return False


#Multiply
#input

r1,c1=list(map(int,input().split()))
p=[]
for i in range(r1):
    l=list(map(int,input().split()))
    p.append(l)
r2,c2=list(map(int,input().split()))
q=[]
for i in range(r2):
    k=list(map(int,input().split()))
    q.append(k)
    
if(validity(p) and validity(q)):
    if(c1==r2):
        w=[[0 for _ in range(c2)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    w[i][j]+=p[i][k]*q[k][j]
        for i in w:
            print(*i)
                    
            
    


    
    
    
    