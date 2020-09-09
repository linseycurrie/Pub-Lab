from src.food import Food

class Customer:

    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def pay_for(self, drink):
        self.wallet -= drink.price
        self.drink(drink)


    def say_age(self):
        return self.age

    def drink(self, drink):
        self.drunkenness += drink.alcohol_level

    def eat(self, food):
        self.drunkenness -= food.rejuvenation_level
        if self.drunkenness < 0:
            self.drunkenness = 0