# class character:
#     def __init__(self, name ,health):
#         self.name = name
#         self.health = health

#     def attack_enemy(self):
#         print(f'{self.name} has {self.health} health')

# warrior = character('thor',43)
# warrior.attack_enemy()


# #Polymorphism

# class Bird():
#     def sound(self):
#         print('Birds make sounds')

# class Crow():
#     def sound(self):
#         print('Crows say "Caw" "Caw"')

# class Parrrot():
#     def sound(self):
#         print('parrots sometimes speak')

# bird1 = Crow()
# bird2 = Parrrot()

# bird1.sound()
# bird2.sound()


#Encapsulation
# hiding at details such as bank account number
# class bankaccount:
#     def __init__(self,accountnum,balance):
#         self.accountnum = accountnum
#         self.__balance = balance #private

#     def deposit(self,amount):
#         self.__balance += amount
#         print(f'Deposited {amount}, New balance {self.__balance}')

#     def get_balance(self):
#         return self.__balance
    
# account = bankaccount('12345',30000)

# print(account.get_balance())


# warrior_name = "thor"
# warrior_health = 100
# warrior_attack = 50


# mage_name = "Gandal"
# mage_health = 80
# mage_attack = 70

# def attack_warrir():
#     print(f'Warrior attacks with power', warrior_attack)

# def attack_mage():
#     print(f"mage attacks with power", mage_attack)


# attack_warrir()
# attack_mage()