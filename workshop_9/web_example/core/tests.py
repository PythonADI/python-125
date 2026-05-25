from django.core.exceptions import ValidationError
from django.test import TestCase

from core.models import Product


class ProductTotalValueTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            barcode="1",
            name="test product",
            description="test",
            price=10,
            quantity=12,
            unit=Product.Unit.L,
            color="blue"
        )

    def test_total_inventory_value(self):
        self.assertEqual(self.product.get_total_inventory_value(), 120)


    def test_sell_item(self):
        self.product.sell(10)
        self.assertEqual(self.product.quantity, 2)
        self.product.sell()
        self.assertEqual(self.product.quantity, 1)

        self.product.sell(5)
        self.assertEqual(self.product.quantity, -4)

    def test_naming(self):
        with self.assertRaises(ValidationError):
            p = Product(
                barcode="1",
                name="test product55",
                description="test",
                price=10,
                quantity=12,
                unit=Product.Unit.L,
                color="blue"
            )
            p.full_clean()
