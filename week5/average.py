num = []
loopnum = int(input("ให้ป้อนค่ากี่ตัว : "))
for i in range(1,loopnum+1,1): # ไม่ต้องใส่ ตัวเริ่มต้นก็ได้
    num1 = int(input(f"ใส่ตัวเลขที่ {i} : "))
    num.append(num1)
print(f"ค่าเฉลี่ยของ {num} = {sum(num)//loopnum}")