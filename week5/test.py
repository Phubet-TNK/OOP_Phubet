# ของ list
# a = [12,4245,535,65,76,8]
# # a.append(24) เพิ่ม
# # a.insert(2,655) เพิ่ม แทรก
# # a.remove(12) ลบตัวที่เป็นเลขใน list เช่น 12,4245,535
# # a.pop(2) ลบลำดับที่อยู่ในlist เช่น 0,1,2,3
# del a()
# print(a)
def work2(fun1,sum1,delsum):
    while True:
        if fun1 > 0:
            sum1 += fun1
            print(f"บวก : {sum1}")
            return sum1
        elif fun1 < 0:
            delsum += fun1
            print(f"ลบ : {delsum}")
            return delsum
        
sum1 = 0
delsum = 0
while True:
    fun1 = int(input("ใส่เลข : "))
    if fun1 > 0:
        sum1 = work2(fun1,sum1,delsum)
    elif fun1 < 0:
        delsum = work2(fun1,sum1,delsum)
    else:
        break