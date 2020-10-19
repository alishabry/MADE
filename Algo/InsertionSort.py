n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    for j in range(i, n):
        if lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
print(' '.join(map(str, lst)))