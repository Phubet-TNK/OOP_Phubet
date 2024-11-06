num = int(input("เอาเลขอะไรดี : "))
i = 1
while i <= 24:
    sum = num *i
    if sum / 2 %2 != 0:
        print(f'{num}x{i}={sum}')
    i += 1