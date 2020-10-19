int(input())
lst = list(map(int, input().split()))
 
 
def merge(l, r):
    merge_lst = []
    i, j = 0, 0
    while len(merge_lst) < len(r) + len(l):
        if j == len(r) or(i < len(l) and l[i] <= r[j]):
            merge_lst.append(l[i])
            i += 1
        else:
            merge_lst.append(r[j])
            j += 1
    return merge_lst
   
 
def merge_sort(lst):
    l, r = lst[:len(lst)//2], lst[len(lst)//2:]
    if len(lst) == 1:
        return lst
    l = merge_sort(l)
    r = merge_sort(r)
    return merge(l, r)
  
print(' '.join(map(str, merge_sort(lst))))