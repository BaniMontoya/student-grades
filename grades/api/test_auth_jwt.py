from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def test_authentication(self):
        # Login and get token
        login_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        access_token = response.data['access']
        refresh_token = response.data['refresh']

        # Use refresh token to get new access token
        refresh_data = {'refresh': refresh_token}
        url = reverse('token_refresh')
        response = self.client.post(url, data=refresh_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        new_access_token = response.data['access']
