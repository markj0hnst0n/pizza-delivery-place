from django.test import TestCase
from .forms import OrderForm
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from menu.models import MenuItem, Category
from timeslot.models import Timeslot


class TestOrderFrom(TestCase):

    def test_full_name_is_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_postcode_is_required(self):
        form = OrderForm({'postcode': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('postcode', form.errors.keys())
        self.assertEqual(
            form.errors['postcode'][0], 'This field is required.')

    def test_fields_are_explicit_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('full_name', 'email',
                                            'phone_number', 'street_address1',
                                            'street_address2',
                                            'town_or_city', 'postcode',
                                            'county', 'delivery_info'))
