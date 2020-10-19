def count(lst,  s):
    cnt = {key: 0 for key in s} 
    for i in lst:
        if i in s:
            cnt[i] += 1
    return cnt
 
 
def list_comp(a, b):
    b = b.values()
    a = a.values()
    return sum(map(lambda x, y: x <= y, a, b)) == len(a)
 
[n, m] = list(map(int, input().split(' ')))
l = input()
w = input()
 
inter = list(set(l))
q = 1
l1 = l[0]
cnt = 0
c = count(w, inter)
c2 = count(l1, inter)
q = 1
 
while q <= n:  
    if list_comp(c2, c):
        cnt += len(l1) 
        if q < n:
            l1 += l[q] 
            c2[l[q]] += 1
        q += 1
    else:
        c2[l1[0]] -= 1
        l1 = l1[1:]
        
print(cnt)
 