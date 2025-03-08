class SinhVien:
    ma_sinh_vien = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.id = SinhVien.ma_sinh_vien
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb
        SinhVien.ma_sinh_vien += 1

    def xep_loai_hoc_luc(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.ten}, Giới tính: {self.gioi_tinh}, Ngành: {self.chuyen_nganh}, Điểm TB: {self.diem_tb}, Học lực: {self.xep_loai_hoc_luc()}"

danh_sach_sv = []

def them_sinh_vien():
    ten = input("Nhập tên sinh viên: ")
    gioi_tinh = input("Nhập giới tính: ")
    chuyen_nganh = input("Nhập chuyên ngành: ")
    diem_tb = float(input("Nhập điểm trung bình: "))
    sv = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb)
    danh_sach_sv.append(sv)
    print("Thêm sinh viên thành công!")


def cap_nhat_sinh_vien():
    ma_sv = int(input("Nhập ID sinh viên cần cập nhật: "))
    for sv in danh_sach_sv:
        if sv.id == ma_sv:
            sv.ten = input("Nhập tên mới: ")
            sv.gioi_tinh = input("Nhập giới tính mới: ")
            sv.chuyen_nganh = input("Nhập chuyên ngành mới: ")
            sv.diem_tb = float(input("Nhập điểm trung bình mới: "))
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy sinh viên!")


def xoa_sinh_vien():
    ma_sv = int(input("Nhập ID sinh viên cần xoá: "))
    global danh_sach_sv
    danh_sach_sv = [sv for sv in danh_sach_sv if sv.id != ma_sv]
    print("Xóa thành công!")


def tim_kiem_sinh_vien():
    ten = input("Nhập tên sinh viên cần tìm: ").lower()
    ket_qua = [sv for sv in danh_sach_sv if ten in sv.ten.lower()]
    if ket_qua:
        for sv in ket_qua:
            print(sv)
    else:
        print("Không tìm thấy sinh viên!")


def sap_xep_theo_diem_tb():
    ds_sap_xep = sorted(danh_sach_sv, key=lambda sv: sv.diem_tb, reverse=True)
    for sv in ds_sap_xep:
        print(sv)


def sap_xep_theo_chuyen_nganh():
    ds_sap_xep = sorted(danh_sach_sv, key=lambda sv: sv.chuyen_nganh)
    for sv in ds_sap_xep:
        print(sv)


def hien_thi_danh_sach():
    if not danh_sach_sv:
        print("Danh sách sinh viên trống!")
    else:
        for sv in danh_sach_sv:
            print(sv)


while True:
    print("\nQUẢN LÝ SINH VIÊN")
    print("1. Thêm sinh viên")
    print("2. Cập nhật sinh viên")
    print("3. Xóa sinh viên")
    print("4. Tìm kiếm sinh viên")
    print("5. Sắp xếp theo điểm trung bình")
    print("6. Sắp xếp theo chuyên ngành")
    print("7. Hiển thị danh sách")
    print("8. Thoát")

    lua_chon = input("Chọn chức năng: ")
    if lua_chon == '1':
        them_sinh_vien()
    elif lua_chon == '2':
        cap_nhat_sinh_vien()
    elif lua_chon == '3':
        xoa_sinh_vien()
    elif lua_chon == '4':
        tim_kiem_sinh_vien()
    elif lua_chon == '5':
        sap_xep_theo_diem_tb()
    elif lua_chon == '6':
        sap_xep_theo_chuyen_nganh()
    elif lua_chon == '7':
        hien_thi_danh_sach()
    elif lua_chon == '8':
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
