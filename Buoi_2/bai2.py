def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
chuoi = input("Nhap chuoi muon dao nguoc : ")
print("Chuoi sau khi dao nguoc : ",dao_nguoc_chuoi(chuoi))