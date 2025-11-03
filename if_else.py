import math

from IPython.terminal.shortcuts.auto_suggest import accept

# Doi nhiet do
# F = (9/5)*C + 32

# c = int(input("Input temperature in Celsius: "))
# f = c * (9/5) + 32
# print("Temperature in Fahrenheit is:", "%.2f" % f)

# x1, y1, x2, y2 = map(float, input("Input coordinates of two points (x1 y1 x2 y2): ").split())
# result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print("Distance between the two points is:", '%.2f' % result, math.pow(result, 2))

# a, b, c = map(int, input("three sides of a triangle: ").split())
# if a + b < c or a + c < b or b + c < a:
#     print("No triangle")
# elif a == b and b == c:
#     print ("Equilateral triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle")
# elif math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2) or math.pow(a, 2) + math.pow(c, 2) == math.pow(b, 2) or math.pow(b, 2) + math.pow(c, 2) == math.pow(a, 2):
#     print("Square triangle")
# else:
#     print("triangle")


# change day
# day = int(input("Input days: "))
# year = day // 365
# week = (day - year * 365) // 7
# if week >= 1:
#     day = day % 365 - week * 7
# else:
#     day = day % 365
# print("Year:", year, "Week:", week, "Day:", day)

# Buy water bottles
# little bottle : n,  a : money a little , b : money of two little => least money

# n, a, b = map(int, input("Input n, a, b: ").split())
# if b < 2 * a:
#     price = (n // 2) * b + a if (n %  2 == 1)  else (n // 2) * b
# else :
#     price = a * n
#
# print("price: ", price)

# IN ra chu cai tiep theo in thuong
# A : 65 , a : 97
# char = input("Input a char: ")
# ascii_char = ord(char)
#
# if (ascii_char == 90 or ascii_char == 122):
#     res = "a"
# else:
#     res = chr(ascii_char + 33 ) if ascii_char >= 65 and ascii_char <= 90 else chr(ascii_char + 1)
#
# print(res)
# print(ord(char))

# Domino
# m, n = map(int, input("Input m,n: ").split())
# tich = m * n
# res = tich // 2 if tich % 2 == 0 else int(tich / 2) + 1
# print(res)

# Lát đá quảng trường
# n, m, a = map(int, input("Input n, m, a: ").split())
# res_n = n // a if n % a == 0 else n // a + 1
# res_m = m // a if m % a == 0 else m // a + 1
# print ( "result", res_n * res_m)

#Frog
# a, b, k = map(int, input("Input a, b, k: ").split())
# # X + a , x - b
# res =  k // 2 * (a - b) if k % 2 == 0 else (k // 2 * (a - b) + a)
# # print(a, b, k, (k * a - k * b ) // 2,  (k * a - k * b ) // 2 + a)
# print("Vi tri cua frog: ",res )

n, m = map(int, input("Input n, m: ").split())
min_step = n / 2 if n % 2 == 0 else n // 2 + 1
max_step = n
if m > max_step:
    res = -1
else:
    res = min_step if min_step % m == 0 else int(min_step // m + 1) * m

print("res: ", res)