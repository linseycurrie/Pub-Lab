import pdb

class Pub:

    def __init__(self, name, till, stock):
        self.name = name
        self.till = till
        self.stock = stock

    def sell_drink(self, drink, customer):
        if customer.say_age() >= 18 and customer.drunkenness <= 4:
            self.till += drink.price
            customer.pay_for(drink)
            self.remove_stock(drink)
        elif customer.say_age() < 18:
            print("Sorry you are too young!")
        else:
            print("Sorry, you are too drunk!")

    def sell_food(self, food, customer):
        customer.pay_for(food)
        self.till += food.price
        self.remove_stock(food)


    def remove_stock(self, item):
        index = 0
        while index < (len(self.stock) -1):
            if self.stock[index].name == item.name:
                break
            index += 1
        del(self.stock[index])   
        

    def stock_value(self):
        total = 0 
        for item in self.stock:
            total += item.price
        return total