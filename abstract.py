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
    
# from abc import ABC, abstractmethod


# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class car(Vehicle):

#     def go(self):
#         print("Car goooooo")
    
#     def stop(self):
#         print("Car stopppp")


# class motorbike(Vehicle):

#     def go(self):
#         print("motobike goooo")

#     def stop(self):
#         print("motorbike stawppp")


# class boat(Vehicle):

#     def go(self):
#         print("Boat is goinggg")
    
#     def stop(self):
#         print("Boat stopped")


# Car = car()
# Car.go()
# Car.stop()

# Motorbike = motorbike()
# Motorbike.go()
# Motorbike.stop()

# beet = boat()
# beet.go()
# beet.stop()


from abc import ABC, abstractmethod

class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

class PremiumUserDiscount(DiscountStrategy):
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8

class DiscountEngine:
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)

        return min(prices)

if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)
    print(f"Best price for {product.name} for {user_tier} user: ${best_price}")
    
