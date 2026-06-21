# A
a = 5
b = a
a = 10
print(a, b)   # ? 10 10 

# B
a = [1, 2, 3]
b = a
a.append(4)
print(a, b)   # ? 1 2 3 4 

# C
a = [1, 2, 3]
b = a
a = a + [4]   # Khác gì với .append?
print(a, b)   # ?[ 1, 2, 3 ,4] [1, 2, 3]

# D
a = [1, 2, 3]
b = a
a += [4]      # Tương đương a.extend([4])
print(a, b)   # ? ← Tricky! [ 1, 2, 3 ,4] [1, 2, 3]

def collect_users(name, users=[]):
    users.append(name)
    return users

result1 = collect_users("Alice")
result2 = collect_users("Bob")
result3 = collect_users("Charlie")
print(result3)   # Output sẽ là gì? Giải thích.










# C++ style:
nums = [1, 2, 3, 4, 5]
if len(nums) != 0:
    print("Not empty")

if nums: 
    print("Not empty")

name = ""
if name == "":
    print("No name")

if not name == 0: 
    print("No name")

x = None
if x == None:
    print("Null")

if x is None: 
    print("Null")

count = 0
for n in nums:
    if n % 2 == 0:
        count = count + 1
print("Even count: " + str(count))

for n in nums: 
    if not n % 2: 
        count += 1


def find_max(numbers: list[int]) -> int| None:
    if not numbers:
        return None

    result = numbers[0]

    for n in numbers:
        if n > result:
            result = n

    return result