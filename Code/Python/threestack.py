
# single array -- three stacks    
# three stack

n = 3*5
strts = [0, int(n/3), int(2*n/3)]
tops = [0-1, int(n/3)-1, int(2*n/3)-1]
ends = [int(n/3)-1, int(2*n/3)-1, n]
where_min = [None] * 3
s = [None]*(n+1)

def s3_push(wstack, obj):
    if tops[wstack] is ends[wstack]:
        print("no room to push on this stack")
    else:
        tops[wstack] +=1
        s[tops[wstack]] = obj
    if not where_min[wstack]:
        where_min[wstack] = tops[wstack]
    elif obj < s[where_min[wstack]]:
        where_min[wstack] = tops[wstack]

def s3_min(wstack):
    if not where_min[wstack] is None:
        return s[where_min[wstack]]
    print("nothing in this stack -- so no min")

def s3_pop(wstack):
    if tops[wstack] < strts[wstack]:
        print("nothing to pop on this stack")
        return None
    else:
        out = s[tops[wstack]]
        s[tops[wstack]] = None
        tops[wstack] -=1
    if tops[wstack] < strts[wstack]:
        where_min[wstack] = None
    elif where_min[wstack] > tops[wstack]:
        where_min[wstack] = strts[wstack]
        for i in range(strts[wstack]+1, tops[wstack]+1):
            if s[i] < s[where_min[wstack]]:
                where_min[wstack] = i                       
    return out

def s3_peek(wstack):
    if tops[wstack] < strts[wstack]:
        return None
    return s[tops[wstack]]
    



