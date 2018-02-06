def offset(i):
    for j in range(i):
        for k in range(j+1):
            i -= 1
            if i == 0:
                return j

offset(11)

buckets = [0]*20

def pour(i, amount):
    avail = i - buckets[i-1]
    if amount <= avail:
        buckets[i-1] += amount
    else:
        spill = amount - avail
        buckets[i-1] = i
        o=offset(i)
        pour(i+o+1, spill/2)
        pour(i+o+2, spill/2)
        
pour(1,120)
buckets
