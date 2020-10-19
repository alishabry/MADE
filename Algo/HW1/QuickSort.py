int(input())
ls = list(map(int, input().split()))
 
 
def swap(lst, f, s):
    tmp = lst[s]
    lst[s] = lst[f]
    lst[f] = tmp
    return lst
 
 
def part(lst, l, r):
    i, j = l, r
    m = (lst[l] + lst[r])/2
    while i <= j:
        while lst[i] < m:
            i += 1
        while lst[j] > m:
            j -= 1
        if i >= j:
            break
        lst = swap(lst, i, j)
        i += 1
        j -= 1   
    return j
 
 
def qsort(lst, l, r):
    if l < r:
        q = part(lst, l, r)
        qsort(lst, l, q)
        qsort(lst, q + 1, r)
    return lst
 
print(' '.join(map(str, qsort(ls, 0, len(ls)-1))))