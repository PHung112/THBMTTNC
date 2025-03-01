try:
    num = int(input("Nhập một số nguyên: "))
    print(f"Số nguyên hợp lệ: {num}")
except ValueError:
    print("Không phải số nguyên hợp lệ")
