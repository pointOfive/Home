

# stack
s = list()
s.append('a')
s.pop()
s

# queue
def serve(l):
    return l[0], l[1:]

q = list()
q.append('a')
out, q = serve(q)
out
q


# set of stacks

n = 3
stack_of_stacks = []
top=[0]

def ss_push(obj):
    if not top[0]:
        stack_of_stacks.append([None] * n)
    stack_of_stacks[-1][top[0]] = obj
    top[0]+=1
    top[0]%=n
    
def ss_pop():
    if not len(stack_of_stacks):
        print("nothing to pop, bruh")
        return None
    if not top[0]:
        out = stack_of_stacks[-1][-1]
        stack_of_stacks[-1][-1] = None
        top[0] = n-1
    else:
        top[0] -= 1
        out = stack_of_stacks[-1][top[0]]
        stack_of_stacks[-1][top[0]] = None
        if not top[0]:
            stack_of_stacks.pop()
    return out

def ss_pop_at(stack):
    if stack > len(stack_of_stacks):
        print("no such stack, brah")
        return None
    if stack == (len(stack_of_stacks)-1):
        return ss_pop()
    
    out = stack_of_stacks[stack][-1]    
    for i in range(stack, len(stack_of_stacks)-1):
        stack_of_stacks[stack][-1] = stack_of_stacks[stack+1][0]
        stack_of_stacks[stack+1] = stack_of_stacks[stack+1][1:]
    stack_of_stacks[len(stack_of_stacks)-1].append(None)
    if stack_of_stacks[len(stack_of_stacks)-1] == [None]*n:
        stack_of_stacks.pop()
    
    top[0] -= 1
    return out

