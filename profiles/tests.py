from django.test import TestCase


class TestProfileViews(TestCase):

    def test_admin_page_display(self):
        response = self.client.get('profiles/admin/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_display(self):
        response = self.client.get('profiles/')
        self.assertEqual(response.status_code, 200)
