import pdb, unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 10.00, 20)
        self.drink = Drink("cosmo", 4.00, 3)
        self.food = Food("burger", 2.00, 10)

    def test_has_name(self):
        self.assertEqual("Joe", self.customer.name)

    def test_has_money(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(20, self.customer.say_age())
    
    def test_is_not_drunk(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_pay_for(self):
        self.customer.pay_for(self.drink)
        amount = self.customer.wallet
        self.assertEqual(6.00, amount)

    def test_eat_sober(self):
        self.customer.eat(self.food)
        self.assertEqual(0, self.customer.drunkenness)

    def test_eat_drunk(self):
        self.customer.drink(self.drink)
        self.customer.eat(self.food)
        self.assertEqual(0, self.customer.drunkenness)

    def test_eat_very_drunk(self):
        self.customer.drink(self.drink)
        self.customer.drink(self.drink)
        self.customer.drink(self.drink)
        self.customer.drink(self.drink)
        self.customer.eat(self.food)
        self.assertEqual(2, self.customer.drunkenness)
