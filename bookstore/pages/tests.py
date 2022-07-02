from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.

class TestHomePage(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def check_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
