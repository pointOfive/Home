AM = [
 [1,1,0,0,0],
 [0,0,0,1,0],
 [0,0,0,0,1],
 [1,1,0,0,0],
 [0,0,1,0,0]]

def path(AM, A, B):
    visited = []
    queued = [A]
    while queued:
        current = queued.pop()# change this to a queue if we want a bfs
        visited.append(current)
        for n,p in enumerate(AM[current]):
            if p and n not in visited and n not in queued:
                if n == B:
                    return True
                else: 
                    queued.append(n)
    return False


                    
