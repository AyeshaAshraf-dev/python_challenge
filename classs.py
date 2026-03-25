# class Student:
#     def __init__(self, name, mark1,mark2,mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
    
#     def average(self):
#         avg = ((self.mark1+self.mark2+self.mark3)/3)
#         print((self.name), "the average is ", avg)



# s1 = Student("ayesha", 39,38,33)
# s1.average()




class Account:
    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    def credit(self, amount):
        self.balance -= amount
        print("Rs", amount ,"was debited")
        print("Total balance: ", self.get_balance())

    def debit(self, amount):
        self.balance += amount
        print("Rs", amount ,"was credtited")
        print("Total balance: ", self.get_balance())

    def get_balance(self):
        return self.balance
  


p1 = Account(400000, 12121)
p1.credit(100)
p1.debit(122)