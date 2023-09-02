from django.test import TestCase
from users.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import curriculum
from .serializers import CurriculumSerializer


class CurriculumListTests(TestCase):

    fixtures = ['test_data.json']
    URL = "/api/v1/curriculums/"

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.admin_user = User.objects.create_user(
            username='adminuser', password='adminpassword', is_staff=True, is_superuser=True
        )
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_get_curriculums(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_curriculum(self):
        new_curriculum_data = {'title': 'New Curriculum',
                               'description': 'New Description'}

        response = self.admin_client.post(
            self.URL, new_curriculum_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(curriculum.objects.filter(
            title='New Curriculum').exists())

        created_curriculum = curriculum.objects.get(title='New Curriculum')

        serializer = CurriculumSerializer(created_curriculum)
        relevant_data = {
            'title': serializer.data['title'],
            'description': serializer.data['description'],
        }

        self.assertEqual(relevant_data, new_curriculum_data)
        created_curriculum.delete()


class CurriculumDetailTests(TestCase):

    fixtures = ['test_data.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.admin_user = User.objects.create_user(
            username='adminuser', password='adminpassword', is_staff=True, is_superuser=True
        )
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_get_curriculum(self):
        # Create a curriculum instance for testing
        test_curriculum = curriculum.objects.create(
            title='Test Curriculum', description='Test Description')

        response = self.client.get(
            f'/api/v1/curriculums/{test_curriculum.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data matches the curriculum data
        serializer = CurriculumSerializer(test_curriculum)
        self.assertEqual(response.data, serializer.data)

    def test_update_curriculum(self):
        # Create a curriculum instance for testing
        test_curriculum = curriculum.objects.create(
            title='Test Curriculum', description='Test Description')

        updated_data = {'title': 'Updated Curriculum',
                        'description': 'Updated Description'}

        response = self.admin_client.put(
            f'/api/v1/curriculums/{test_curriculum.id}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve the updated curriculum from the database
        updated_curriculum = curriculum.objects.get(id=test_curriculum.id)

        # Check if the curriculum data was updated as expected
        self.assertEqual(updated_curriculum.title, updated_data['title'])
        self.assertEqual(updated_curriculum.description,
                         updated_data['description'])

    def test_delete_curriculum(self):
        # Create a curriculum instance for testing
        test_curriculum = curriculum.objects.create(
            title='Test Curriculum', description='Test Description')

        response = self.admin_client.delete(
            f'/api/v1/curriculums/{test_curriculum.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the curriculum was deleted from the database
        self.assertFalse(curriculum.objects.filter(
            id=test_curriculum.id).exists())
