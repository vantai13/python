#  tong phan tu trong mang vi tri l - r
# goi y: dung mang cong don f[0] = a[0] , f[i] = f[i - 1] = a[i]
def sum_array(n, a, l, r):
    f = [0] * 100000001
    f[0] = a[0]
    for i in range(1, n):
        f[i] = f[i - 1] + a[i]



    result = f[r - 1] - f[l - 1 - 1]
    print("result: ", result)

    for i in range(n):
        print(f[i], end = " ")






if __name__ == "__main__":
    n = int(input("Input n: "))
    a = list(map(int, input("Intput a: ").split()))
    l = int(input("input l: "))
    r = int(input("input r: "))

    sum_array(n, a, l , r)



