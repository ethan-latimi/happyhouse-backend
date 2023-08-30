from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import curriculum


class CurriculumTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.curriculum_data = {
            "title": "Mathematics",
            "description": "Math curriculum description.",
            "photo": "http://example.com/photo.jpg"
        }
        self.curriculum = curriculum.objects.create(**self.curriculum_data)

    def test_get_all_curriculums(self):
        response = self.client.get('/curriculums/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_curriculum(self):
        response = self.client.get(f'/curriculums/{self.curriculum.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.curriculum_data['title'])

    # You can add more test methods for POST, PUT, DELETE, etc.
