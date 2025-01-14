class Prodcut:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price= price
        self.__stock = stock
    def AddStock(self,add):
        self.__stock += add
    def editprice(self,edit):
        self.__price = edit
    def CheckProduct(self):
        return f"ชื่อสินค้า {self.name} ราคา {self.__price} จำนวน {self.__stock}"
# pd1 = Prodcut("สินค้า1",400,5)
# pd1.price = 399
# print (pd1.CheckProduct())
# # pd2 = Prodcut("สินค้า2",500,10)
# # print (pd2.CheckProduct())
class Phone(Prodcut):
    def __init__(self, name, price, stock,system):
        super().__init__(name, price, stock)
        self.system = system
    def showPhone(self):
        return f"ประเภท {self.system} มี {super().CheckProduct()}"
class Notbook(Prodcut):
    def __init__(self, name, price, stock,system):
        super().__init__(name, price, stock)
        self.system = system
    def showNotbook(self):
        return f"ประเภท {self.system} มี {super().CheckProduct()}"
class Cloth(Prodcut):
    def __init__(self, name, price, stock,fabric):
        super().__init__(name, price, stock)
        self.fabric = fabric
    def showCloth(self):
        return f"ประเภท {self.fabric} มี {super().CheckProduct()}"
print("----------------------------------------------")
Phone1 = Phone("samsung A58",10000,12,'Android')
print(Phone1.showPhone())
print("----------------------------------------------")
Notbook1 = Notbook("Notebook Asus Vivobook 16 ",19900,10,'windows 11 home')
print(Notbook1.showNotbook())
print("----------------------------------------------")
Cloth1 = Cloth("ROMWE Anime",240,100,'ผ้ายืด')
print(Cloth1.showCloth())
print("----------------------------------------------")
