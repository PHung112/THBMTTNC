list_so = input("Nhập dãy số được ngăn cách bằng dấu phẩy : ")
so = list(map(int,list_so.split(",")))

dem = {}

for dem_so in so:
    if dem_so in dem:
        dem[dem_so] += 1
    else :
        dem[dem_so] = 1

print("Số lần xuất hiện của mỗi phần tử : ",dem)