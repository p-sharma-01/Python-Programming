class MatrixDimensionError(Exception):
    pass

class Matrix:
    def __init__(self, data):
        self.data = data  # 2D list

    # Implement these
    def __add__(self, other):
        r1,c1=(len(self.data),len(self.data[0]))
        w=[[0 for _ in range(c1)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c1):
                w[i][j]=self.data[i][j]+other.data[i][j]
        print(w)
    
    def __mul__(self, other):
        r1,c1=(len(self.data),len(self.data[0]))
        r2,c2=(len(other.data),len(other.data[0]))
        w=[[0 for i in range(c2)] for j in range(r1)]
        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    w[i][j]+=self.data[i][k]*other.data[k][j]
        print(w)
    
    def __eq__(self, other):
        c=0
        for i,j in zip(self.data,other.data):
            if i==j:
                c+=1
        if c==0:
            return False
        return True
                
            
    
    @property
    def transpose(self):
        r1,c1=(len(self.data),len(self.data[0]))
        w=[[0 for i in range(r1)] for j in range(c1)]
        for i in range(r1):
            for j in range(c1):
                w[i][j]=self.data[j][i]
        print(w)

# Test Input
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[5,6],[7,8]])
m1+m2
m1*m2
m1.transpose
print(m1.__eq__(m2))


# print((m1 + m2).data)  # [[6,8],[10,12]]
# print((m1 * m2).data)  # [[19,22],[43,50]]
# print(m1.transpose.data)  # [[1,3],[2,4]]
# functionality
# technical complexity
# creativity and innovation
# UI/UX
# scability and performanca
# presentation/ round