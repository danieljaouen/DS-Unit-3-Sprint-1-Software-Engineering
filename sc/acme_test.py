#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explode(self):
        """Test default stealability and explode."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable...')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """Making sure the Acme Report is correct."""
    def test_default_num_products(self):
        """Test default num products is 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test legal names."""
        products = generate_products()
        valid_names = [first + ' ' + second for first in ADJECTIVES for second in NOUNS]
        [self.assertIn(product.name, valid_names) for product in products]


if __name__ == '__main__':
    unittest.main()
