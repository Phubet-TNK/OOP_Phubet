class Library:
    def __init__(self,username):
        self.namebook = [] #list
        self.username = username
    def add_book(self):
        while True:
            book = {} # dict
            book["name"] = str(input("เพิ่มหนังสือ หากต้องการหยุดให้พิมพ์ 'หยุด': "))
            if book["name"] == 'หยุด':
                break
            else:
                book["page"] = int(input("ใส่จำนวนหน้าหนังสือ : "))
                book["price"] = int(input("ใส่ราคาของหนังสือ : "))
                self.namebook.append(book)
                print("-------------------------------------------")
    def show_book(self):
        for show in self.namebook: # ใส่ ['name'] ไม่ได้ เพราะ มันติด int เพระมันรวมทั้ง dict
            print(show) #เอาแค่ชื่อก็แค่ใส่ ['name'] ไปข้างหลัง show
    def find_book(self):
        findname = str(input('ค้นหาชื่อ:'))
        for find in self.namebook:
            if findname == find['name']:
                print(find)
book1 = Library("one")
book1.add_book()
book1.show_book()
book1.find_book()