num = int(input("เอาเลขอะไรดี: "))
for i in range(1,25,1):
    sum = num * i 
    if sum/2 % 2 == 0:
        continue
    else:
        print(num ,"x",i,"=",sum)