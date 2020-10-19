import sys
 
 
def lower_bound(left, right, x):
    while left != right - 1:    
        mid = (left + right) // 2
        if x <= lst[mid]:
            right = mid
        else:
            left = mid
    return right
    
n = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split(' '))))
m = int(sys.stdin.readline())
for i in range(m):
    [l, r] = list(map(int, sys.stdin.readline().split(' ')))
    sys.stdout.write(str(lower_bound(-1, n, r + 1) - lower_bound(-1, n, l)) + '\n')