import sys
 
 
def approx_bin_search(left, right, x):
    if left == right - 1:
        if x - lst[left] <= lst[right] - x:
            return lst[left] 
        else:
            return lst[right]
    mid = (left + right) // 2
    if x == lst[mid]:
        return lst[mid]
    elif x < lst[mid]:
        return approx_bin_search(left, mid, x)
    else:
        return approx_bin_search(mid, right, x)
    
[n, m] = list(map(int, sys.stdin.readline().split(' ')))
lst = list(map(int, sys.stdin.readline().split(' ')))
k = list(map(int, sys.stdin.readline().split(' ')))
 
for i in k:
    sys.stdout.write(str(approx_bin_search(0, n - 1, i)) + '\n')