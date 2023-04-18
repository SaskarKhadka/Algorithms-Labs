import math

def merge(data, p, q, r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(n1):
        L.append(data[p+i])
    for j in range(n2):
        R.append(data[q+j+1])

    L.append(math.inf)
    R.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            data[k] = L[i]
            i = i+1
        else:
            data[k] = R[j]
            j = j+1

def merge_sort(data, p, r):
    if p < r:
        q = (p+r) // 2
        merge_sort(data, p, q)
        merge_sort(data, q+1, r)
        merge(data, p, q, r)


