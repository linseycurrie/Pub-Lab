import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("beer", 2.50, 3)

    def test_has_name(self):
        self.assertEqual("beer", self.drink.name)

    def test_has_price(self):
        self.assertEqual(2.50, self.drink.price)

    def test_has_alcohol_level(self):
        self.assertEqual(3, self.drink.alcohol_level)
