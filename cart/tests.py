from django.test import TestCase
from menu.models import MenuItem


class TestCartViews(TestCase):

    def test_cart_page_display(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart(self):
        test_item = MenuItem.objects.create(
            name='Test Menu Item', price='1.00')
        response = self.client.post(f'/add/{test_item}')
        self.assertEqual(response.status_code, 200)

    def test_adjust_cart_item(self):
        test_item = MenuItem.objects.create(
            name='Test Menu Item', price='1.00')
        response = self.client.post(f'/adjust/{test_item}')
        self.assertEqual(response.status_code, 200)

    def test_remove_cart_item(self):
        test_item = MenuItem.objects.create(
            name='Test Menu Item', price='1.00')
        response = self.client.post(f'/remove/{test_item}')
        self.assertEqual(response.status_code, 200)
