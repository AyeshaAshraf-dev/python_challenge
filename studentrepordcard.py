
class Student:
    def __init__(self, name, rollnum):
        self.name = name
        self.rollnum = rollnum
        self.marks = {}

    def add_subject(self,subject, num):
        self.marks[subject] = num

    def update_marks(self, subject,num):
        self.marks.update({subject: num})

    def delete_subject(self, subject):
        if subject in self.marks:
            del self.marks[subject]
        else:
            print("It does not exist")
    def grade(self):
       if self.average() >= 90:
           return "A"
       elif self.average() >= 80:
           return "B"
       elif self.average() >= 75:
           return "C"
       elif self.average() >= 65:
           return "D"
       elif self.average() >= 50:
           return "D-"
       elif self.average() >= 40:
           return "E"
       else:
           return "F"


    def average(self):
        if not self.marks:
            return "Empty! "
        total = sum(self.marks.values())
        count = len(self.marks)
        return total/count
        
    def pass_fail(self):
        if self.average() < 40:
            return f"Fail"
        else:
            return f"Pass"

    def __str__(self):
        return f"-------WELCOME--------"
    def report_card(self):
        print(f"--------Official Report for {self.name}-----------")
        print("-------Personal Information--------")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollnum}")
        print("-----Marks Information------")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")
        print("-----------------------")
        print(f"Average marks: {self.average()}")
        print(f"Status: {self.pass_fail()}")
        print(f"Grade: {self.grade()}")
        if self.pass_fail() == "Pass":
            print("Remarks: \nGood Efforts! Keep it up Dear!")
        else:
            print("Remarks: \nNeed more Efforts! Just remember kid that u can do it!")



s1 = Student("Ayeza Ishaan", 22)
# print(s1)
s1.add_subject("English", 87)
s1.add_subject("Chem", 77)
s1.add_subject("Physics", 65)
s1.add_subject("Math", 44)
s1.add_subject("Computer", 54)
s1.report_card()
# s1.delete_subject("math")
s1.average()

s2 = Student("Soniya Rohan", 12)
# print(s1)
s2.add_subject("English", 22)
s2.add_subject("Chem", 21)
s2.add_subject("Physics", 33)
s2.add_subject("Math", 12)
s2.add_subject("Computer", 14)
s2.report_card()
# s1.delete_subject("math")
s2.average()