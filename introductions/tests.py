from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import introduction  # Import your Introduction model
# Import your IntroductionSerializer
from .serializers import IntroductionSerializer


class IntroductionTests(APITestCase):

    fixtures = ['test_data.json']
    URL = "/api/v1/introductions/"

    def setUp(self):
        self.client = APIClient()

    def test_create_introduction(self):

        new_introduction_kind = "preschool"
        new_introduction_description = "new desc"
        data = {'kind': new_introduction_kind,
                'description': new_introduction_description}
        response = self.client.post(
            self.URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
