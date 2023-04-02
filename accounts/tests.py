from lib.tests import APITestMixin


class AccountTests(APITestMixin):
    def test_signup(self):
        r = self.send_post(
            'signup',
            {
                'first_name': 'test_user',
                'email': 'test@gmail.com',
                'password': 'password'
            }
        )
        self.assertEquals(r.status_code, 201)

    def test_reset_password(self):
        r = self.send_post(
            'reset-password',
            {
                'old_password': self.TEST_PASSWORD,
                'new_password_1': 'new_password',
                'new_password_2': 'new_password'
            },
            authorize=True
        )
        print(r.request)

        print(r.data)

