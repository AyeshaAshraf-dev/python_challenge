# from abc import ABC, abstractmethod


# #Abstraction hides unnessasary details
# #parent class act as a blueprint 
# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         print("hy")

# class Car(vehicle):
#     def start(self):
#         print("Car starts with key")

# class Bike(vehicle):
#     def start(self):
#         print("bike do hup")

# car = Car()
# bike = Bike()

# car.start()
# bike.start()
    
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class car(Vehicle):

    def go(self):
        print("Car goooooo")
    
    def stop(self):
        print("Car stopppp")


class motorbike(Vehicle):

    def go(self):
        print("motobike goooo")

    def stop(self):
        print("motorbike stawppp")


class boat(Vehicle):

    def go(self):
        print("Boat is goinggg")
    
    def stop(self):
        print("Boat stopped")


Car = car()
Car.go()
Car.stop()

Motorbike = motorbike()
Motorbike.go()
Motorbike.stop()

beet = boat()
beet.go()
beet.stop()
