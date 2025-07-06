import unittest
from shopping_cart import CalculateTotal

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total_valid_prices(self):
        cart = [
            {'name': 'Item A', 'price': 10.00},
            {'name': 'Item B', 'price': 5.50}
        ]
        self.assertAlmostEqual(CalculateTotal(cart), 15.50)

    def test_calculate_total_empty_cart(self):
        cart = []
        self.assertEqual(CalculateTotal(cart), 0)

    def test_calculate_total_with_invalid_price_type(self):
        cart = [{'name': 'Broken Item', 'price': '9.99'}]
        with self.assertRaises(TypeError):
            CalculateTotal(cart)

if __name__ == '__main__':
    unittest.main()
