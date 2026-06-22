# A. In ra index và giá trị
nums = [10, 20, 30, 40]
i = 0
while i < len(nums):
    print(i, nums[i])
    i += 1

# B. Cộng 2 list
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])

# C. Lặp ngược và in
nums = [1, 2, 3, 4, 5]
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])

# D. Lọc số dương từ list
nums = [-3, 1, -4, 2, -5, 6]
positives = []
for n in nums:
    if n > 0:
        positives.append(n)

# E. Tạo dict bình phương 0-9
squares = {}
i = 0
while i < 10:
    squares[i] = i * i
    i += 1