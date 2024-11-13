box = {"nickname":"","stdid":"","hobby":"","color":""}
loopnum = int(input("จำนวนคนที่จะป้อน : "))
for i in range(loopnum):
    print(f"กรุณากรอกข้อมูลคนที่ {i+1}")
    nickname = input("กรุณาใส่ชื่อเล่น : ")
    box["nickname"] = nickname
    stdid = input("กรุณากรอกเล่นที่ : ")
    box["stdid"] = stdid
    hobby = input("กรุณากรอกงานอดิเรก : ")
    box["hobby"] = hobby
    color = input("กรุณากรอกสีที่ชอบ : ")
    box["color"] = color
    print(f"ข้อมูลคนที่ {i+1}\n{box}\n-----------------------------------")
