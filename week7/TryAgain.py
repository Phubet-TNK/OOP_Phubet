shop = 0
stcok = 0
while True:
    try:
        stcok +=1
        num = input(f"ใส่ราคาสินค้าที่ {stcok} : ")
        if num == "exit":
            break
        num = int(num)
        shop += num
        if num == 0:
            raise ZeroDivisionError()
        elif num <0:
            raise Exception()
        else:
            print(f"สินค้าที่ {stcok}\nราคาสินค้านี้คือ : {num} บาท")
            print("-----------------------------")
    except ZeroDivisionError:
        print("ราคาสินค้าต้องมากว่า 0")
    except ValueError:
        print("กรูณาใส่ตัวเลขเท่านั้น")
    except:
        print("ราคาสินค้าต้องไม่ติดลบ")
print(f"ยอดรวมสินค้าทั้งหมด {shop} บาท\nสินค้าทั้งหมด {stcok} สินค้า")