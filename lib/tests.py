from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class APITestMixin(APITestCase):
    fixtures = ['fixtures/accounts.json', 'fixtures/products.json']
    TEST_EMAIL = 'admin@gmail.com'
    TEST_PASSWORD = 'admin'

    def send_request(self, reverse_url, data=None, headers=None, is_get=False):
        url = reverse(reverse_url)

        if not headers:
            headers = {}

        if is_get:
            return self.client.get(url, headers=headers)

        return self.client.post(url, data=data, headers=headers)

    def send_get(self, reverse_url):
        return self.send_request(reverse_url, is_get=True)

    def send_post(self, reverse_url, data, authorize=False):
        if authorize:
            headers = {}
            # token = self.test_login()
            # headers = {'Authorization': f'Bearer {token}'}
            a = self.client.login(email=self.TEST_EMAIL, password=self.TEST_PASSWORD)
        else:
            headers = {}

        return self.send_request(reverse_url, data, headers=headers)

    def test_login(self):
        r = self.send_post(
            'login',
            {
                'email': self.TEST_EMAIL,
                'password': self.TEST_PASSWORD
            }
        )

        self.assertEquals(r.status_code, 201)
        return r.data.get('token')

