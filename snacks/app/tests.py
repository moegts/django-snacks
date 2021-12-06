from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.


class SnacksTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        acutal_status_code = self.client.get(url).status_code
        self.assertEqual(acutal_status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        acutal_status_code = self.client.get(url).status_code
        self.assertEqual(acutal_status_code, 200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
