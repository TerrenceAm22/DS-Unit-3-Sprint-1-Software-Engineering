import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):
    """ Making sure Acme Products are the tops!
    """
def test_default_product_price(self):
    """Test default product price being 10.
    """
    prod = Product('Test Product')
    self.assertEqual(prod.price,10)
    return

if __name__ == '__main__':
    unittest.main(test_default_product_price)
