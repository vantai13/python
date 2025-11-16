# liêt ke so nguyen to trong list
from math import *
def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

# tim max , min
def max_min( a):
    max_val = a[0]
    min_val = a[0]
    for x in a:
        if max_val <= x:
            max_val = x
        if min_val >= x:
            min_val = x
    return max_val, min_val

# tong bang 10
if __name__ == '__main__':
    n = int(input("Input n: "))
    a = list(map(int, input().split()))
    for x in a:
        tmp = 10 - x
        if len()



