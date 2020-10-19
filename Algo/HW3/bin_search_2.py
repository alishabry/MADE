def count(t, x, y):
    return 1 + t // x + t // y 
 
 
def bin_search(x, y, n):
    left = 0
    right = n * (max(x, y) + 1) 
    if n == 1:
        return min(x, y)
    while left < right - 1:
        mid = (left + right) // 2
        if n <= count(mid, x, y):
            right = mid
        else:
            left = mid
    return min(x, y) + right
 
[n, x, y] = list(map(int, input().split(' ')))
 
print(bin_search(x, y, n))