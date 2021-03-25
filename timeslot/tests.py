from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from menu.models import MenuItem, Category
from timeslot.models import Timeslot


class TestTimeslotViews(TestCase):

    def setUp(self):
        new_timeslot = Timeslot.objects.create(
            pk=1,
            available_slots=1
        )

    def test_view_timeslot(self):
        response = self.client.get(reverse('timeslot'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timeslot/timeslot.html')
    
    def test_book_a_slot_when_its_already_booked(self):
        session = self.client.session
        session['slot'] = {'1': True}
        session.save()

        response = self.client.post(reverse(
                                'book_a_slot',
                                kwargs={'s_id': 1}))
        
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("You've booked a slot already")

        self.assertRedirects(response, '/menu/')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)
    
    def test_book_a_slot(self):
        response = self.client.post(reverse(
                                'book_a_slot',
                                kwargs={'s_id': 1}))
        
        messages = list(get_messages(response.wsgi_request))
        expected_message = ("Slot booked in!")

        self.assertRedirects(response, '/menu/')
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)
    
    def test_timeslot_refresh(self):
        response = self.client.get(reverse('timeslot_refresh'), follow=True)
        self.assertRedirects(response, '/home/')
        

    def tearDown(self):
        new_timeslot = Timeslot.objects.get(pk=1)

        del new_timeslot
