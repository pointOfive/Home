a=[1]
b=[1,2] # -> [1,1]
#b=[2,1] # -> [1,1]
#b=[1,1] # -> [2,0]
b=[2,2,3,3,5] # -> [0,2]

i=0
while i < len(b):
    cur = b[i]
    if cur <= 0:
        i += 1
    else:
        if b[cur-1] <= 0:
            b[cur-1] -= 1
            b[i] = 0
            i += 1
        else:
            b[i],b[cur-1] = b[cur-1], -1
b
