try:
    num1 = int(input("ใส่ยอดชำระ : "))
    discount20 = num1*0.2
    discount10 = num1*0.1
    if num1 == 0:
        raise ZeroDivisionError()
    elif num1 < 0:
        raise Exception()
    elif num1 >= 5000:
        print("คุณได้รับส่วนลด 20% ยอดชำระที่ต้องจ่ายคือ ",num1-discount20)
    elif num1 >=2000 :
        print("คุณได้รับส่วนลด 10% ยอดชำระที่ต้องจ่ายคือ ",num1-discount10)
    else:
        print("คุณไม่ได้รับส่วนลด")
except ValueError:
    print("ป้อนเฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามป้อนค่า 0")
except:
    print("ห้ามป้อนค่าติดลบ")