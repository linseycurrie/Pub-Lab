import pdb, unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Joe", 10.00, 20)

    def test_has_name(self):
        self.assertEqual("Joe", self.customer.name)

    def test_has_money(self):
        self.assertEqual(10.00, self.customer.wallet)

    def test_has_age(self):
        self.assertEqual(20, self.customer.age)
    
    def test_is_not_drunk(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_pay(self):
        self.customer.pay(5.00)
        amount = self.customer.wallet
        self.assertEqual(5.00, amount)