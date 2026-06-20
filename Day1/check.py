"""
🎯 PHẦN 9: BÀI TẬP TƯ DUY
Bài tập 1: Quan sát và giải thích
Chạy đoạn code sau và giải thích kết quả:
pythona = 256
b = 256
print(a is b)   # Kết quả?

x = 1000
y = 1000
print(x is y)   # Kết quả? Khác bài trên không? Tại sao?
Hint: Google "Python integer caching" sau khi bạn đã tự nghĩ.
Bài tập 2: Dự đoán output
pythonlist1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

list1.append(4)

print(list1)   # ?
print(list2)   # ?
print(list3)   # ?
Trước khi chạy, viết ra giấy dự đoán của bạn. Sau đó chạy và xem có đúng không.

Bài tập 3: Câu hỏi suy nghĩ (không cần code)
Một công ty đang chọn ngôn ngữ cho 3 dự án:

Dự án A: Game engine cần render 144 FPS
Dự án B: Script tự động deploy server hàng ngày
Dự án C: Mô hình AI dự đoán giá nhà

Theo bạn, dự án nào nên dùng C++, dự án nào nên dùng Python? Tại sao?
Bài tập 4: Câu hỏi phỏng vấn thực tế
"Em hãy giải thích tại sao Python chậm hơn C++, và tại sao Python vẫn được dùng nhiều trong AI?"
Hãy viết ra câu trả lời của bạn (như đang phỏng vấn) — khoảng 3-5 câu — sau đó so sánh với câu trả lời mẫu ở phần đầu lesson.

"""


a = 256 
b = 256 
print(a is b)

c = 1000
d = 1000
print ( c is d)

list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

list1.append(4)

print(list1)   # ? 1 2 3 4 
print(list2)   # ? 1 2 3 4 
print(list3)   # ? 1 2 3 