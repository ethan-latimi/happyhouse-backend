from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from .models import Introduction
from .serializers import IntroductionSerializer


class IntroductionTests(APITestCase):

    fixtures = ['test_data.json']
    URL = "/api/v1/introductions/"

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

    def test_get(self):
        response = self.client.get(f'/api/v1/introductions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_introduction(self):

        new_introduction_kind = "preschool"
        new_introduction_description = "new desc"
        data = {'kind': new_introduction_kind,
                'description': new_introduction_description}
        response = self.admin_client.post(
            self.URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class IntroductionDetailTests(APITestCase):
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
        self.intro = Introduction.objects.create(
            kind=Introduction.BusinessChoices.preschool, description='Test Introduction')

    def test_get_object(self):
        response = self.client.get(f'/api/v1/introductions/{self.intro.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Test Introduction')

    def test_get(self):
        response = self.client.get(f'/api/v1/introductions/{self.intro.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = IntroductionSerializer(self.intro)
        self.assertEqual(response.data, serializer.data)

    def test_put(self):
        updated_data = {'kind': Introduction.BusinessChoices.housing,
                        'description': 'Updated Introduction'}
        response = self.admin_client.put(
            f'/api/v1/introductions/{self.intro.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.intro.refresh_from_db()
        self.assertEqual(self.intro.kind, Introduction.BusinessChoices.housing)
        self.assertEqual(self.intro.description, 'Updated Introduction')

    def test_put_unauthenticated(self):
        updated_data = {
            'kind': Introduction.BusinessChoices.housing,
            'description': 'Updated Introduction'
        }
        response = self.client.put(
            f'/api/v1/introductions/{self.intro.pk}/', updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_authenticated(self):

        self.client.login(username='adminuser', password='adminpassword')

        updated_data = {
            'kind': Introduction.BusinessChoices.housing,
            'description': 'Updated Introduction'
        }
        response = self.client.put(
            f'/api/v1/introductions/{self.intro.pk}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.client.login(username='adminuser', password='adminpassword')
        response = self.client.delete(
            f'/api/v1/introductions/{self.intro.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Introduction.DoesNotExist):
            self.intro.refresh_from_db()
