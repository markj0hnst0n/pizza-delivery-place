from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from menu.models import MenuItem, Category


class TestCartViews(TestCase):

    def setUp(self):
        new_category = Category.objects.create(
            name='test_category',
            friendly_name='test category',
        )

        new_product = MenuItem.objects.create(
            category=new_category,
            name='test product',
            price=1.00
            )

    def test_view_cart(self):
        response = self.client.get(reverse('cart'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart_with_no_timeslot(self):
        new_product = MenuItem.objects.get(name='test product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'add_to_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("You need to book a timeslot first!")

        self.assertRedirects(response, '/timeslot/')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = MenuItem.objects.get(product_name='test product')

        del new_category
        del new_product
