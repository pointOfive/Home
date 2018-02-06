from collections import defaultdict
a = list(range(1,20))
a = a + a + [0, 20]
d = defaultdict(int)
d = dict()
for i in a:
    if i in d:
        del d[i]
    else:
        d[i] = 1
    
d
