"""
🎯 PHẦN 6: BÀI TẬP
Bài tập 1: Refactor sang Pythonic
Viết lại các đoạn sau theo phong cách Pythonic:
python# A.
nums = [1, 2, 3, 4, 5]
i = 0
while i < len(nums):
    print(i, nums[i])
    i = i + 1

# B.
name = input("Tên: ")
if name == "":
    name = "Anonymous"

# C.
def get_grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            return "C"

# D.
a = 5
b = 10
temp = a
a = b
b = temp

# E.
x = 50
if x >= 0:
    if x <= 100:
        print("Valid")
Bài tập 2: Đoán output
python# A.
print(0 or "fallback")
print(5 or "fallback")
print("" or 0)
print(None or False or "" or "found")

# B.
print(True and "yes")
print(False and "yes")
print([] and "yes")

# C.
a, b, c = 1, 5, 3
print(a < b < c)
print(a < b > c)
print(c < a < b)

# D.
n = 5
result = "even" if n % 2 == 0 else "odd"
print(result)

# E.
matrix = [[0] * 3] * 3
matrix[0][0] = 99
print(matrix)
Bài tập 3: f-string master
Viết f-string in ra như sau:

Pi với 4 chữ số thập phân, padding 10 ký tự
Số 42 dưới dạng binary, hex, octal
Tỷ lệ 0.875 dưới dạng phần trăm 2 chữ số
Debug print biến user_count = 100 ở format user_count=100

Bài tập 4: LeetCode-style input
Viết code đọc input có format:
3
1 2 3
4 5 6
7 8 9
(Dòng đầu là n, sau đó là ma trận n x n số int)
Lưu vào biến matrix và in tổng tất cả các phần tử.
Bài tập 5: FizzBuzz Pythonic
Viết FizzBuzz (1 → 30):

Chia hết 3 → "Fizz"
Chia hết 5 → "Buzz"
Chia hết cả 2 → "FizzBuzz"
Còn lại → số đó

Yêu cầu: Code phải CÀNG PYTHONIC CÀNG TỐT. Cố gắng dưới 10 dòng.
Bài tập 6: Câu hỏi phỏng vấn
"Em hãy giải thích short-circuit evaluation trong Python. Cho ví dụ và ứng dụng thực tế."
Viết câu trả lời + 2 ví dụ code.
Bài tập 7: Tìm bug
pythondef create_users(usernames, default_role="user"):
    return [{"name": u, "role": default_role} for u in usernames]

users = create_users(["alice", "bob"])
print(users)

# Câu hỏi:
# 1. Code này có bug "mutable default argument" không?
# 2. Tại sao có/không?
"""

nums = [1, 2, 3, 4, 5]
i = 0
# while i < len(nums):
#     print(i, nums[i])
#     i = i + 1

for i,  num in enumerate(nums, start=0):
    print(i, num)

name = input("Tên: ")
if name == "":
    name = "Anonymous"
print(name)

name = input("Tên: ") or "Anonymous"
print(name)


def get_grade(score):
    if score >= 90:
        return "A"
    else:
        if score >= 80:
            return "B"
        else:
            return "C"
        
score = int(input("input score: "))       
get_grade = "A" if score >=90 else "B" if score >= 80 else "C"

a = 5
b = 10
temp = a
a = b
b = temp

a,b = b, a 


x = 50
if x >= 0:
    if x <= 100:
        print("Valid")

if  0 <= x <= 100: 
    print("valid")


# A.
print(0 or "fallback") # 0
print(5 or "fallback") #
print("" or 0)
print(None or False or "" or "found")

# B.
print(True and "yes")
print(False and "yes")
print([] and "yes")

# C.
a, b, c = 1, 5, 3
print(a < b < c)
print(a < b > c)
print(c < a < b)

# D.
n = 5
result = "even" if n % 2 == 0 else "odd"
print(result)

# E.
matrix = [[0] * 3] * 3
matrix[0][0] = 99
print(matrix)