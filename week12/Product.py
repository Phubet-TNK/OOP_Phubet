class Prodcut:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock
    def AddStock(self,add):
        self.__stock += add
    def CheckProduct(self):
        return f"ชื่อสินค้า {self.name} ราคา {self.__price} จำนวน {self.__stock}"
    def editprice(self,edit):
        self.__price = edit

pd1 = Prodcut("สินค้า1",400,5)
pd1.AddStock(-1)
pd1.editprice(1200)
print (pd1.CheckProduct())