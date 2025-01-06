class Product:
    def __init__(self):
        self.products = {}
    def add_product(self):
        while True:
            name_product = input("ชื่อสินค้า : ")
            if name_product == "หยุด":
                break
            else:
                __price = int(input("ราคา: "))
                __stock = int(input("จำนวนสินค้า: "))
                self.products[name_product] = (__price, __stock)
    def show_products(self):
        for name_product, product_info in self.products.items():
            __price, __stock = product_info
            print(f"ชื่อ: {name_product}, ราคา: {__price}, จำนวนสินค้า: {__stock}")
    def changeprice(self):
        name_product = input("ใส่ชื่อสินค้าที่ต้องการ เปลี่ยนราคา ")
        if name_product in self.products:
            new_price = int(input("ราคา : "))
            __price, __stock = self.products[name_product]
            self.products[name_product] = (new_price, __stock)
            print(f"ราคาสินเค้า {name_product}: {new_price}")
    def addproduct(self):
        name_product = input("ใส่ชื่อสินค้าที่ต้องการ เพิ่มจำนวน : ")
        if name_product in self.products:
            stock = int(input("จำนวนสินค้า : "))
            __price, __stock = self.products[name_product]
            self.products[name_product] = (__price, __stock + stock)
            print(f"สินค้าจำนวน {name_product}: {__stock + stock}")
    def delproduct(self):
        name_product = input("ใส่ชื่อสินค้าที่ต้องการ ลบจำนวน : ")
        if name_product in self.products:
            reduction_stock = int(input("จำนวนสินค้า : "))
            __price, __stock = self.products[name_product]
            if reduction_stock <= __stock:
                self.products[name_product] = (__price, __stock - reduction_stock)
                print(f"สินค้าจำนวน {name_product}: {__stock - reduction_stock}")
my_product = Product()
my_product.add_product()
my_product.show_products()
my_product.addproduct()
my_product.show_products()
my_product.delproduct()
my_product.show_products()
my_product.changeprice()
my_product.show_products()