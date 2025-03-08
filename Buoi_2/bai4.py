list_so = input("Nhập dãy số được ngăn cách bằng dấu phẩy : ")
so = list(map(int,list_so.split(",")))

mang_tuple = tuple(so)

phan_tu_dau_tien = mang_tuple[0]
phan_tu_cuoi_cung = mang_tuple[-1]

print("Phần tử đầu tiên trong mảng : ",phan_tu_dau_tien)
print("Phần tử cuối cùng trong mảng : ",phan_tu_cuoi_cung)