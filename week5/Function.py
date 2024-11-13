def fun1(num1,num2):
    box = []
    for i in range(num1,num2+1,1):
        if i %3 != 0:
            box.append(i)
    return box


def fun2(num,sum1,delsum):
    while True:
        if num > 0:
            sum1 += num
            print(f"ผลบวก : {sum1}")
            return sum1
        elif num < 0:
            delsum += num
            print(f"ผลลบ : {delsum}")
            return delsum