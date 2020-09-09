import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("burger", 2.00, 10)

    def test_has_name(self):
        self.assertEqual("burger", self.food.name)

    def test_has_price(self):
        self.assertEqual(2.00, self.food.price)

    def test_has_rejuvenation_level(self):
        self.assertEqual(10, self.food.rejuvenation_level)


    