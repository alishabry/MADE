import math
 
 
def f(x):
    return x**2 + math.sqrt(x) 
 
 
def bin_search(y):
    left = 0
    right = 1
    while f(right) < y:
        right *= 2
    itn = int(math.log(right / 10**(-6), 2)) + 1
    for i in range(itn):
        mid = (left + right) / 2
        if f(mid) < y:
            left = mid
        else:
            right = mid
    return right
 
print(bin_search(float(input())))