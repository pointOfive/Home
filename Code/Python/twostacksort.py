
# sort stack with stack

def bubble(depth, a, b=[]):
    if depth==0:
        return

    for i in range(depth):
        b.append(a.pop())
        
    if a[-1]<b[-1]:
        a.append(b.pop())
    else:
        tmp = a.pop()
        a.append(b.pop())
        a.append(tmp)

    for i in range(depth-1):
        a.append(b.pop())

    return bubble(depth-1, a, b=[])

a = list(range(10,0,-1))
for i in range(len(a)-1):
    bubble(len(a)-1, a, b=[])


# trying it out:

def bubble2(a, b=[]):
    for j in range(1, len(a)):
        b.append(a.pop())
        for i in range(0,len(a)-j+1):
            if a[-1]<b[-1]:
                b.append(a.pop())
            else:
                tmp = b.pop()
                b.append(a.pop())
                b.append(tmp)
        for i in range(len(b)):
            a.append(b.pop())

a = list(range(10,0,-1))
bubble2(a, b=[])

