import math
 
 
def time(x):
    l1 = math.sqrt((1 - a) ** 2 + x ** 2)
    l2 = math.sqrt((1 - x) ** 2 + a ** 2)
    return l1 / v1 + l2 / v2
    
 
def tren_search():
    left = 0
    right = 1
    itn = 1000
    for i in range(itn):
        m1 = left + (right - left) / 3
        m2 = right - (right - left) / 3
        if time(m1) < time(m2):
            right = m2
        else:
            left = m1
    return left
 
[v1, v2] = list(map(int, input().split(' ')))
a = float(input())
 
print(tren_search())