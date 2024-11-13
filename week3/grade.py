num = int(input("ป้อนเกรด : "))
if num > 100 :
    print("ใส่เกรดให้ถูกต้อง")
elif num < 0 :
    print("ใส่เกรดให้ถูกต้อง")
elif (num >= 80)==(num <= 100) :
    print("ได้เกรด 4")
elif (num >= 70)==(num <= 79) :
    print("ได้เกรด 3")
elif (num >= 60)==(num <= 69) :
    print("ได้เกรด 2")
elif (num >= 50)==(num <= 59) :
    print("ได้เกรด 1")
else:
    num <= 49
    print("ได้เกรด 0")
    fix = str(input("ต้องการที่จะแก้คะแนนหรือไม ถ้าใช้ พิมพ์ Y ถ้าไม่ พิมพ์ N : "))
    if fix == "Y" :
        print("ยังขาดคะแนนอีก :",50-num)
    elif fix == "N":
        print("สอบตกเหมือนเดิม")
    else:
        print("ป้อนคำตอบให้ถูกต้อง")