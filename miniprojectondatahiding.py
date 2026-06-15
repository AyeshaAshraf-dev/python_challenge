class BankAccount:
    def __init__(self, holder_name, starting_balance):
        self.holder_name = holder_name;
    
        if starting_balance >= 0:
            self.__balance = starting_balance
        else:
            print("Not sufficient balance")

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if (amount>0):
            self.__balance += amount
        else:
            print("INVALID")


amount = BankAccount("isha", 3000)

print(amount.get_balance())
amount.deposit(500)