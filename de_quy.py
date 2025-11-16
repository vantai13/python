# Tinh tong
def tong(n):
    if n == 0 :
        return 0
    return n + tong(n - 1)

# so fibonacci
def fibo(n):
    if n == 1 : return 0
    if n == 2 : return 1
    return fibo(n - 1) + fibo(n - 2)

# luy thua
def luy_thua(a,b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return pow(a,b//2) * pow(a,b//2)
    else :
        return pow(a,b//2) * pow(a,b//2) * pow(a,b)

if __name__ == "__main__":
    # n = int(input("Input n: "))
    # print(f"Fibo thu {n} là :{fibo(n)} ")

    a, b = map(int, input("Input a, b: ").split())
    print("luy thua a, b la :", luy_thua(a, b))

