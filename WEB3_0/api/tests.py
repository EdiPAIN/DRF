from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User_Model

class MoneyTransferTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.source_user = User_Model.objects.create(User_Name="Alice", User_IIN="123456789012", All_money=1000.0)
        self.target_user = User_Model.objects.create(User_Name="Bob", User_IIN="987654321012", All_money=500.0)

    def test_transfer_money(self):
        url = reverse('Transfer')
        data = {
            'source_inn': self.source_user.User_IIN,
            'target_inn': self.target_user.User_IIN,
            'amount': 200.0,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 302)
        self.source_user.refresh_from_db()
        self.target_user.refresh_from_db()
        self.assertEqual(self.source_user.All_money, 800.0)
        self.assertEqual(self.target_user.All_money, 700.0)


class UserListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse('Create')
        data = {
            'User_Name': 'Eve',
            'User_IIN': '111122223333',
            'All_money': 100.0,
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, 200)
        user = User_Model.objects.get(User_Name='Eve')
        self.assertEqual(user.User_IIN, '111122223333')
        self.assertEqual(user.All_money, 100.0)
