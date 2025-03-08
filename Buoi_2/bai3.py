list_so = input("Nhập dãy số được ngăn cách bằng dấu phẩy : ")
numbers = list(map(int,list_so.split(",")))

mang_tuple = tuple(numbers)
print("Mảng tuple :",mang_tuple)
