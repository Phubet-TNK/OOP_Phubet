import random
scorewin = 0
scorelose = 0
scorealways = 0
while True:
    bot = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(bot)
    uesr = str(input("กรุณาเลือก ค้อน กรรไกร กระดาษ หากต้องการหยุด ให้พิมพ์ หยุด\nคุณเลือกคือ : "))
    if uesr == bot:
        print("ผลลัทธ์คือ : เสมอ")
        scorealways +=1
    elif (bot == "ค้อน") and (uesr == "กระดาษ") or (bot == "กระดาษ") and (uesr == "กรรไกร") or (bot == "กรรไกร") and (uesr == "ค้อน"):
        print("ผลลัทธ์คือ : คุณชนะ")
        scorewin +=1
    elif uesr == "หยุด":
        print(f'ผลรวมทั้งหมด\nชนะ {scorewin} \tแพ้ {scorelose} \tเสมอ {scorealways} รวมคะแนนทั้งหมด {scorewin+scorelose+scorealways}')
        break
    else:
        print("ผลลัทธ์คือ : คุณแพ้")
        scorelose +=1
    print("-----------------------------")