
# queue as two stacks

ins = [1,2]
out = []
mode = 'in'
q = {'in': ins, 'out': out}

def flip():
    if mode == 'in':
        q['out'] = q[mode][-1::-1]
        q[mode] = []
        return 'out'
    else:
        q['in'] = q[mode][-1::-1]
        q[mode] = []
        return 'in'
        
def ssq_push(obj):
    if mode == 'in':
        q[mode].append(obj)
        tmp = mode
    else:
        tmp = flip()
        q[tmp].append(obj)

    return tmp

def ssq_exit():
    if mode == 'out':
        tmp2=q[mode].pop()
        tmp = mode
    else:
        tmp = flip()
        tmp2 = q[tmp].pop()

    return tmp, tmp2

