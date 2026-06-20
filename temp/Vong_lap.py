from math import *

# for i in range(1, 10, 1):
#     print(i)

# 21
# Tong uoc cua so nguyen duong N

# n = int(input("Input n: "))
#
# uoc_dem = 0

# for i in range (1, n + 1, 1):
# #     if n % i == 0:
# #         print("Uoc cua n la:", i)
# #         uoc_dem += i

# cach 2

# for i in range(1, int(n ** (1/2)) + 1, 1):
#
#     if n % i == 0:
#       print(f"Uoc cua {n} la: {i} và {n // i}")
#       uoc_dem += i if n / i == i else i + n // i
#       print("uoc dem la: ", uoc_dem)
#
# print("Tong uoc dem cua n la :{}".format(uoc_dem))

# so chinh phuong
# n = int(input("Input n: "))
#
# for i in range (2, int(sqrt(n)) + 1, 1):
#     print(i ** 2 , end= " ")
#     tmp = i ** 2
#     if tmp ** (1/2) == i:
#         print(i ** 2, end=" ")

# kiem tra so nhap vao co 1307

# n = int(input("Nhap n: "))
# i = 1
# while (n):
#     n -=1
#     k = int(input(f"Nhap vao so thu {i}: "))
#     if k == 1307:
#         print("correct")
#         break
#     i += 1
# if i == 4:
#     print("No")

# dem so luong chu so cua n
# n = int(input("nhap n: "))
# dem = 0
# if n == 0:
#     dem = 1
# else :
#     while (n):
#         n = n // 10
#         dem += 1
# print("tong so luong chu so cua n: ", dem)

# mua bia
# n = int(input("Nhap tien: "))
# chai_bia = n // 28
# res = 0
# chai_bia_du = 0
# while (chai_bia <= 3):
#     res += chai_bia
#     chai_bia_du =  chai_bia % 3
#     chai_bia = chai_bia // 3 + chai_bia_du
# res += chai_bia_du
# print(res)

# n = int(input("Nhap n: "))
#
# chai_bia = n // 28
# res = chai_bia
# vo_bia = chai_bia
#
# while (vo_bia >= 3):
#     vo_bia_du = vo_bia % 3
#     chai_bia = vo_bia // 3
#     res += chai_bia
#     vo_bia = chai_bia + vo_bia_du
#
# print("So luong chai bia toi da la: ", res)


# bieu dien duoi dang so nguyen to
# n = int(input("Input n: "))
# i = 2
#
# dem = 0
# if n == 1 or n == 0:
#     print("-1")
# else:
#     for i in range (2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             while (n % i == 0):
#                 n -= i
#                 print(i, end= " ")
#                 if n < 2:
#                     break
#
#     if n > 2:
#         print(n)

n = int(input("Nhap n: "))
count = 0
if n == 1 or n == 0: 
    print("-1")
else :
    if n % 2 == 0:
        count = n // 2
    else:
        count = n // 2 + 1
    print(count)
    for i in range(0, (n // 2)):
        print("2", end=" ")

    if n % 2 != 0:
        print("3")











