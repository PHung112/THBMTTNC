so_gio_lam = float(input("Nhập số giờ làm :"))
luong_gio = float(input("Nhập lương của mỗi giờ :"))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam-gio_tieu_chuan)
tong_luong = gio_tieu_chuan*luong_gio + gio_vuot_chuan*luong_gio*1.5

print("Tổng lương nhân viên nhận được là :",tong_luong)