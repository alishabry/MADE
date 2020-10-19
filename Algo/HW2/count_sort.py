def count_sort(lst):
    cnt = [0] * (max(lst) + 1)
    for i in lst:
        cnt[i] += 1
    lst = []
    [lst.append([str(j)] * cnt[j]) for j in range(len(cnt)) if cnt[j] > 0]
    print(' '.join(sum(lst, [])))
 
count_sort(list(map(int, input().split(' '))))