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

# Gia tri khac nhau trong mang va liet ke

def array_different(n, a):
    """
    chi ap dung voi so duong
    :param n:
    :param a:
    :return:
    """
    seen = [0] * 100000001
    for x in a:
        seen[x] = 1
    count = 0
    for x in a:
        if seen[x] == 1:
            count += 1
            print(f"{x} ", end="")
            seen[x] = 0
    print("")
    print(f"So luong phan tu khac nhau la: {count}")

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

def sum_k(n, a, k):
    count = [0] * 10000001
    for x in a:
        count[x] += 1
    res = 0
    for x in a:
        if x == k - x:
            count[x] -= 1
            res += count[x]
        elif count[k - x] > 0:
            res += count[k - x]
            count[x] -= 1

    return res

def fibonaci(x):
    fibo = [0] * 93
    fibo[1], fibo[2] = 1, 1
    for i in range(3, 93):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    if x in fibo:
        return 1
    return 0

def min_max_position(n, a):
    pos_min, pos_max, min_val, max_val = 1, 1, a[0], a[0]

    for i in range(n):
        if min_val >= a[i]:
            pos_min = i + 1
            min_val = a[i]
        if max_val < a[i]:
            pos_max = i + 1
            max_val = a[i]
    print(min_val, pos_min)
    print(max_val, pos_max)

def gcd(a, b):
    while b:
        tmp = a % b
        a = b
        b = tmp
    return a

def lien_ke_trai_dau(n, a):
    if a[0] * a[1] < 0 :
        print(a[0], end=" ")

    for i in range(1, n - 1):
        if a[i] * a[i - 1] < 0 or a[i] * a[i + 1] < 0:
            print(a[i], end=" ")
    if a[n - 1] * a[n - 1 - 1] < 0:
        print(a[n - 1])

def min_space(n, a):
    """
    co the sort() roi lam
    :param n:
    :param a:
    :return:
    """

if __name__ == '__main__':
    n = int(input("Input n: "))
    a = list(map(int, input("Input array: ").split()))

    # # Reverse array
    # for i in range(n // 2):
    #     if a[i] != a[n - i - 1]:
    #         print("no")
    #         exit(0)
    #
    # print("yes")

    lien_ke_trai_dau(n, a)





