```python
import unittest
from src.user_account import UserAccount, UserSchema

class TestUserAccount(unittest.TestCase):

    def setUp(self):
        self.user_account = UserAccount()
        self.user_schema = UserSchema()

    def test_signup_user(self):
        test_user_data = {
            'username': 'testUser',
            'password': 'testPassword',
            'email': 'testUser@example.com',
            'preferences': {
                'calendar': 'Google',
                'emailPlatform': 'Gmail'
            }
        }
        result = self.user_account.signupUser(test_user_data)
        self.assertEqual(result, 'signupSuccess')

    def test_login_user(self):
        test_user_data = {
            'username': 'testUser',
            'password': 'testPassword'
        }
        result = self.user_account.loginUser(test_user_data)
        self.assertEqual(result, 'loginSuccess')

    def test_user_schema(self):
        test_user_data = {
            'username': 'testUser',
            'password': 'testPassword',
            'email': 'testUser@example.com',
            'preferences': {
                'calendar': 'Google',
                'emailPlatform': 'Gmail'
            }
        }
        result = self.user_schema.load(test_user_data)
        self.assertEqual(result, test_user_data)

if __name__ == '__main__':
    unittest.main()
```