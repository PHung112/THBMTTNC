def tinh_tong_chan(lst):
    tong = 0
    for num in lst:
        if num%2 == 0:
            tong += num
    return tong

list_so = input("Nhap 1 day so duoc ngan cach bang dau phay :")
numbers = list(map(int,list_so.split(",")))
print("Tong so chan trong list :",tinh_tong_chan(numbers))