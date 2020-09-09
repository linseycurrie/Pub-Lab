import unittest
from src.pub import Pub
from src.drink  import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Bob", 50.00, 30)
        self.drink = Drink("cosmo", 4.00, 3)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(104.00, self.pub.till)
        self.assertEqual(46.00, self.customer.wallet)
