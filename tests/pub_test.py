import unittest
from src.pub import Pub
from src.drink  import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        stock = [
            Drink("cosmo", 4.00, 3),
            Drink("beer", 2.50, 2),
            Food("burger", 2.00, 10),
            Food("hotdog", 2.00, 5)
        ]
        
        self.pub = Pub("The Prancing Pony", 100.00, stock)
        self.customer = Customer("Bob", 50.00, 30)
        self.drink = self.pub.stock[0]
        self.young_customer = Customer("Betty", 20.00, 16)
        self.food = Food("hotdog", 2.00, 5)


    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_sell_drink_correct_age(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(46.00, self.customer.wallet)
        self.assertEqual(3, len(self.pub.stock))

    def test_sell_drink_too_young(self):
        self.pub.sell_drink(self.drink, self.young_customer)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(20.00, self.young_customer.wallet)

    def test_sell_drink_too_drunk(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(108.00, self.pub.till)
        self.assertEqual(42.00, self.customer.wallet)

    def test_stock_value(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(6.5, self.pub.stock_value())

    def test_sell_food(self):
        self.pub.sell_food(self.food, self.customer)
        self.assertEqual(102.00 ,self.pub.till)
        self.assertEqual(48.00, self.customer.wallet)