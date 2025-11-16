from math import *
# tinh tong uoc
from sqlalchemy import false


def tong_uoc(n):
    res = 0
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            # print("i la :",i)
            # print("res la :",res + i + n // i)
            # print("res la :",res + i)
            res = res + i if n / i == i else res + i + n // i
    return res

# kiem tra so nguyen to

def nguyen_to(n):
    if n == 0 or n == 1:
        return 0
    else :
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return 0
    return 1

def thua_so_nguyen_to(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while (n % i == 0):
                print(i, end=" ")
                n //= i

    if n > 1:
        print(n)

# boi chung nho nhat
def gcd(a, b):
    while (b):
        tmp = a % b
        a = b
        b = tmp
    return a

def so_thuan_nghich(n):
    if n < 10 : return 1
    tai = n
    tmp = 0
    while(n):
        last = n % 10
        n //= 10
        tmp = tmp * 10 + last

    print(tmp)
    if tmp == tai :

        return 1
    return 0

def dem_chu_so(n):
    dem = 0
    while (n):
        dem += 1
        n /= 10
    return dem

# def so_hoan_hao(n):

# so luong uoc cua n la so nguyen to
def uoc_nt(n):
    res = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            print(i)
            res = i
            while n % i == 0:
                n /= i
    if n > 1:
        res = n
    return res

# kiem tra xem co phai sphenic hay khong
def sphenic(n):
    sum = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum += 1
            dem = 0
            while n % i == 0:
                n //= i
                dem += 1
                if dem > 1:
                    return 0
    if n > 1:
        sum += 1

    if sum == 3:
        return 1

# phan tich thua so nguyen to in ra 2^2 * 3^2...

def  thua_so_nt(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            if n < 2:
                print(f"{i}^{cnt}")
            else :
                print(f"{i}^{cnt} + ", end="")

    if n > 1:
        print(f"{n}")

# so smith: Khong phai la nguyen to, tong cac chu so = tong chu so thua so nguyen to

def tong_chu_so(n):
    sum = 0
    while n:
        last = n % 10
        n //= 10
        sum += last
    return sum

def smith(n):
    sum = 0
    tmp = n
    sum1 = tong_chu_so(n)
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:

            while n % i == 0:
                n //= i
                sum += tong_chu_so(i)
    if tmp == n :
        return 0
    if n > 1:
        sum += tong_chu_so(n)
    return sum == sum1


if __name__ == '__main__':
    # n = int(input("Input n: "))
    # res = tong_uoc(n)
    # print("Tong uoc cua n la: ", res)

    # if (nguyen_to(n)):
    #     print("yes")
    # else:
    #     print("no")

    # a, b = map(int, input("Nhap a, b: ").split())
    # print(gcd(a, b))



    n = int(input("Input n: "))

    if smith(n):
        print("yes")
    else :
        print("no")
























