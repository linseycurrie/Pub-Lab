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
            #self.stock.remove(drink)
            index = 0
            while index < (len(self.stock) -1):
                if self.stock[index].name == drink.name:
                    break
                index += 1
            del(self.stock[index])
        elif customer.say_age() < 18:
            print("Sorry you are too young!")
        else:
            print("Sorry, you are too drunk!")

    # def remove_drink_from_stock(self, sold_drink):
    #     index = 0
    #     #pdb.set_trace()
    #     while index < len(self.stock["drinks"]):
    #         if self.stock["drinks"][index].name == sold_drink.name:
    #             break
    #         index += 1
    #     del(self.stock["drinks"][index])
        

    def stock_value(self):
        total = 0 
        for item in self.stock:
            total += item.price
        return total