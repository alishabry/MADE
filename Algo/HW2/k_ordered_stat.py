import random
 
 
def part(lst, l, r):
    low, i, high = l, l, r  
    pivot = cl[random.randint(l, r)]             
    while i <= high:      
        if lst[i] < pivot:
            lst[low], lst[i] = lst[i], lst[low]
            low += 1
            i += 1
        elif lst[i] > pivot:
            lst[i], lst[high] = lst[high], lst[i]
            high -= 1
        else:
            i += 1
            
    return low, high
 
 
def qfind(l, r, k):
    if r - l == 0:
        return 0
    low, high = part(cl, l, r)
    if k < low:
        return qfind(l, low, k)
    elif k > high:
        return qfind(high, r, k) 
    else:
        return cl[k]
 
n = int(input())
clones = list(map(int, input().split(' ')))
m = int(input())
for t in range(m):
    [i, j, k] = map(int, input().split(' '))
    cl = clones[i-1:j].copy()
    qfind(0, len(cl) - 1, k - 1)
    print(cl[k-1])