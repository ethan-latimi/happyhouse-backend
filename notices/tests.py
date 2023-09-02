from users.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import notice
from .serializers import NoticeSerializer


class NoticeListTests(APITestCase):

    URL = "/api/v1/notices/"

    def setUp(self):
        self.client = self.client_class()
        self.admin_user = User.objects.create_user(
            username='adminuser', password='adminpassword', is_staff=True, is_superuser=True
        )
        self.admin_client = self.client_class()
        self.admin_client.force_authenticate(user=self.admin_user)

    def test_get_notices(self):
        # Create some notice instances for testing
        notice1 = notice.objects.create(
            title='Notice 1', content='Content for Notice 1')
        notice2 = notice.objects.create(
            title='Notice 2', content='Content for Notice 2')

        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response data contains the titles of the notices
        self.assertContains(response, 'Notice 1')
        self.assertContains(response, 'Notice 2')

    def test_create_notice(self):
        new_notice_data = {'title': 'New Notice', 'content': 'New Content'}

        response = self.admin_client.post(
            self.URL, new_notice_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        try:
            # Check if the notice was created in the database
            self.assertTrue(notice.objects.filter(
                title='New Notice').exists())
        except notice.DoesNotExist:
            pass  # Handle the case where the notice may not exist

        # Clean up: Delete the created notice if it exists
        try:
            created_notice = notice.objects.get(title='New Notice')
            created_notice.delete()
        except notice.DoesNotExist:
            pass  # Handle the case where the notice may not exist
