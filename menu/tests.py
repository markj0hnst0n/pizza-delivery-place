from django.test import TestCase
from .models import MenuItem


class TestMenuItemModel(TestCase):

    def test_veg_defaults_to_false(self):
        item = MenuItem.objects.create(name='Test Item', price='1.00')
        self.assertFalse(item.vegetarian)

    def test_spicy_defaults_to_false(self):
        item = MenuItem.objects.create(name='Test Item', price='1.00')
        self.assertFalse(item.spicy)
