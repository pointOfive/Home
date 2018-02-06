import numpy as np

mat = np.zeros([4,4])

for i in range(4):
    for j in range(4):
        mat[i,j] = j+i*4

mat_rot90=mat.copy()
for i in range(4):
    # could just do row to column
    for j in range(4):
        mat_rot90[j,3-i] = mat[i,j]

# In place
for layer in range(int(n/2)):
    for entry in range(layer,n-layer-1):
        print(layer)
        print(entry)
        tmp = mat[entry, n-1-layer]
        mat[entry, n-1-layer] = mat[layer, entry]
        tmp2 = mat[n-1-layer,n-1-entry]
        mat[n-1-layer,n-1-entry]=tmp
        tmp = mat[n-1-entry,layer]
        mat[n-1-entry,layer] = tmp2
        mat[layer, entry] = tmp

