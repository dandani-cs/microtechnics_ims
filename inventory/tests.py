from django.test import TestCase
from inventory.models import Item

# Create your tests here.
class InventoryTests(TestCase):
    def test_item_quantity_levels(self):
        item = Item( name         = "CUSTOM_ITEM",
                     max_quantity = 100 )

        test_values = [
                    ( 1,  0 ), ( 9,  0 ),
                    ( 11, 1 ), ( 24, 1 ),
                    ( 26, 2 ), ( 99, 2 ),
                ]

        for test in test_values:
            item.quantity = test[0]
            self.assertEqual(item.calc_quantity_level(), test[1])
