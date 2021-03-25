from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from menu.models import MenuItem, Category
from timeslot.models import Timeslot


class TestCartViews(TestCase):

    def setUp(self):
        new_category = Category.objects.create(
            name='test_category',
            friendly_name='test category',
        )

        new_product = MenuItem.objects.create(
            category=new_category,
            name='test_product',
            price=1.00
            )

        new_timeslot = Timeslot.objects.create(
            pk=1,
            available_slots=1
        )

    def test_view_cart(self):
        response = self.client.get(reverse('cart'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart.html')

    def test_add_to_cart_with_no_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
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

    def test_add_to_cart_with_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        session = self.client.session
        session['slot'] = {'1': True}
        session['cart'] = {'1': 1}
        session.save()
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }

        response = self.client.post(reverse(
                                'add_to_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = (f'Added {new_product.name} to cart!')

        self.assertRedirects(response, '/')
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)

    def test_add_more_than_4_to_cart_with_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        session = self.client.session
        session['slot'] = {'1': True}
        session['cart'] = {'1': 5}
        session.save()
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }

        response = self.client.post(reverse(
                                'add_to_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("No more than 4 per item, sorry! :)")

        self.assertRedirects(response, '/cart/')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)

    def test_adjust_cart_with_no_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'adjust_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("You need to book a timeslot first!")

        self.assertRedirects(response, '/timeslot/')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)

    def test_adjust_cart_with_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        session = self.client.session
        session['slot'] = {'1': True}
        session['cart'] = {'1': 1}
        session.save()
        post_data = {
            'quantity': '3',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'adjust_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = (f'Updated {new_product.name} quantity to 3')

        self.assertRedirects(response, '/cart/')
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)

    def test_adjust_cart_to_zero_with_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        session = self.client.session
        session['slot'] = {'1': True}
        session['cart'] = {'1': 1}
        session.save()
        post_data = {
            'quantity': '0',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'adjust_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = (f'Removed {new_product.name} from shopping cart')

        self.assertRedirects(response, '/cart/')
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)

    def test_remove_from_cart_with_no_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        post_data = {
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse(
                                'remove_from_cart',
                                kwargs={'item_id': new_product.id}),
                                data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("You need to book a timeslot first!")

        self.assertRedirects(response, '/timeslot/')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)

    def test_remove_from_cart__with_timeslot(self):
        new_product = MenuItem.objects.get(name='test_product')
        session = self.client.session
        session['slot'] = {'1': True}
        session['cart'] = {'1': 1}
        session.save()
        response = self.client.post(reverse(
                                'remove_from_cart',
                                kwargs={'item_id': new_product.id})
                                )
        messages = list(get_messages(response.wsgi_request))
        expected_message = (f'Removed {new_product.name} from shopping cart')


        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = MenuItem.objects.get(name='test_product')
        new_timeslot = Timeslot.objects.get(pk=1)

        del new_category
        del new_product
        del new_timeslot
