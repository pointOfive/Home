import numpy as np

mat = np.zeros([4,4])

for i in range(4):
    for j in range(4):
        mat[i,j] = j+i*4
        
Srow=set()
Scol=set()

for i in range(n):
    for j in range(n):
        if mat[i,j] == 0:
            Srow.add(i)
            Scol.add(j)        
        
for i in Srow:
    mat[i,:]=0

for j in Scol:
    mat[:,j]=0

    
