dict_so = {0: "zero",1: "one",2: "two"}

key_xoa = int(input("Nhập key cần xoá : "))
if key_xoa in dict_so:
    del dict_so[key_xoa]
    print("Dict sau khi xoá : ",dict_so)
else:
    print("Key cần xoá k tồn tại.")