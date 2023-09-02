from users.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import notice
from .serializers import NoticeSerializer


class NoticeListAPITestCase(APITestCase):

    URL = "/api/v1/notices/"

    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_user(
            username='adminuser', password='adminpassword', is_staff=True, is_superuser=True
        )
        self.admin_client = APIClient()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_get_notice_list(self):

        # Create some test notices
        notice1 = notice.objects.create(
            title="Notice 1", content="Content 1")
        notice2 = notice.objects.create(
            title="Notice 2", content="Content 2")

        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the serialized notices
        serialized_data = NoticeSerializer([notice1, notice2], many=True).data
        self.assertEqual(response.data, serialized_data)

    def test_create_notice(self):
        data = {
            "title": "New Notice",
            "content": "New Content",
        }

        response = self.admin_client.post(self.URL, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the notice has been created in the database
        notice_obj = notice.objects.filter(title="New Notice").first()
        self.assertIsNotNone(notice_obj)

    def test_unauthorized_create_notice(self):
        data = {
            "title": "New Notice",
            "content": "New Content",
        }

        # Create a non-staff user
        non_staff_user = User.objects.create_user(
            username="nonstaffuser",
            password="nonstaffpassword"
        )

        # Authenticate as the non-staff user
        self.client.force_authenticate(user=non_staff_user)

        response = self.client.post(self.URL, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
