stri="thisismystringandiwantthemaxlengthsubstringwithnoduplicates"
best = 0,0,0
i = 0 
while i < len(stri)-2:
    cur = set(stri[i])
    for j in range(i+2, len(stri)):
        if stri[j] not in cur:
            cur.add(stri[j])
            if j-i+1 > best[0]:
                best = j-i+1, i, j
                print(stri[best[1]:best[2]+1])
        else:
            while stri[i] != stri[j]:
                i += 1
            break
    i += 1
print(best)
stri[best[1]:best[2]+1]
