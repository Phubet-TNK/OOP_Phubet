import random as r
class Student:
    def __init__(self,ชื่อนามสกุล,ชื่อเล่น):
        self.name = ชื่อนามสกุล
        self.nickname = ชื่อเล่น
        self.score = 0
        self.grade = ""
    def score0(self):
        self.score = r.randint(1,10)
    def Grade(self):
        if self.score >= 5:
            self.grade ="คุณผ่าน"
        else:
            self.grade ="คุณไม่ผ่าน"

Student1 = Student("Phubet Deenu","Film1")
Student1.score0()
Student1.Grade()
Student2 = Student("Phubet Deenu","Film2")
Student2.score0()
Student2.Grade()
Student3 = Student("Phubet Deenu","Film3")
Student3.score0()
Student3.Grade()
Student4 = Student("Phubet Deenu","Film4")
Student4.score0()
Student4.Grade()
Student5 = Student("Phubet Deenu","Film5")
Student5.score0()
Student5.Grade()

print("คนที่ 1")
print(f"{Student1.name} {Student1.nickname} {Student1.score} คะแนน {Student1.grade}")
print("-----------------------------------------")
print("คนที่ 2")
print(f"{Student2.name} {Student2.nickname} {Student2.score} คะแนน {Student2.grade}")
print("-----------------------------------------")
print("คนที่ 3")
print(f"{Student3.name} {Student3.nickname} {Student3.score} คะแนน {Student3.grade}")
print("-----------------------------------------")
print("คนที่ 4")
print(f"{Student4.name} {Student4.nickname} {Student4.score} คะแนน {Student4.grade}")
print("-----------------------------------------")
print("คนที่ 5")
print(f"{Student5.name} {Student5.nickname} {Student5.score} คะแนน {Student5.grade}")
print("-----------------------------------------")