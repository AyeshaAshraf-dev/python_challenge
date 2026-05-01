class character:
    def __init__(self, name ,health):
        self.name = name
        self.health = health

    def attack_enemy(self):
        print(f'{self.name} has {self.health} health')

warrior = character('thor',43)
warrior.attack_enemy()


#Polymorphism

class Bird():
    def sound(self):
        print('Birds make sounds')

class Crow():
    def sound(self):
        print('Crows say "Caw" "Caw"')

class Parrrot():
    def sound(self):
        print('parrots sometimes speak')

bird1 = Crow()
bird2 = Parrrot()

bird1.sound()
bird2.sound()









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