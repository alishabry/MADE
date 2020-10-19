def count(r_len, lst, k):
    return k <= sum([i // r_len for i in lst]) 
 
 
def bin_search(lst, k):
    left = max(lst) // k
    right = max(lst) + 1 
    while left < right - 1: 
        mid = (left + right) // 2
        if count(mid, lst, k):
            left = mid
        else:
            right = mid
    return left
 
[n, k] = list(map(int, input().split(' ')))
lst = [int(input()) for i in range(n)]
 
print(bin_search(lst, k))