
class Pub:

    def __init__(self, name, till):
        self.name = name
        self.till = till

    def sell_drink(self, drink, customer):
        self.till += drink.price
        customer.pay(drink.price)