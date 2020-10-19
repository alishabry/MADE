def count_sort(lst):
    l = list(map(lambda x: x[1], lst))
    p = [0] * (ord('z'))   
    cnt = [0] * (ord('z') + 1)   
    for i in l:
        cnt[i] += 1
    for i in range(1, len(cnt)-1):
        p[i] += cnt[i-1] + p[i-1]
    sorted_lst = [0] * (len(lst))
    for i in range(len(lst)):
        sorted_lst[p[l[i]]] = lst[i]
        p[l[i]] += 1
    return sorted_lst
 
[n, m, k] = list(map(int, input().split(' ')))
l = []
 
for i in range(n):
    l.append(input())
 
for i in range(m-1, m-k-1, -1): 
    l = list(map(lambda y: y[0], count_sort(list(map(lambda x: (x, ord(x[i])-ord('a')), l)))))
 
for i in l:
    print(i)