from abc import ABC, abstractmethod


#Abstraction hides unnessasary details
#parent class act as a blueprint 
class vehicle(ABC):
    @abstractmethod
    def start(self):
        print("hy")

class Car(vehicle):
    def start(self):
        print("Car starts with key")

class Bike(vehicle):
    def start(self):
        print("bike do hup")

car = Car()
bike = Bike()

car.start()
bike.start()
    
