from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import introduction


class IntroductionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.intro_data = {
            "kind": "preschool",
            "description": "This is a description.",
            "photo": "http://example.com/photo.jpg"
        }
        self.intro = introduction.objects.create(**self.intro_data)

    def test_get_all_introductions(self):
        response = self.client.get('/introductions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_introduction(self):
        response = self.client.get(f'/introductions/{self.intro.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['kind'], self.intro_data['kind'])
