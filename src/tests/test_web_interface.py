```python
import unittest
from src import web_interface

class TestWebInterface(unittest.TestCase):

    def setUp(self):
        self.web_interface = web_interface.WebInterface()

    def test_loginUser(self):
        response = self.web_interface.loginUser('testUser', 'testPassword')
        self.assertEqual(response, 'loginSuccess')

    def test_signupUser(self):
        response = self.web_interface.signupUser('newUser', 'newPassword')
        self.assertEqual(response, 'signupSuccess')

    def test_scheduleTask(self):
        response = self.web_interface.scheduleTask('testUser', 'testTask')
        self.assertEqual(response, 'scheduleSuccess')

    def test_manageEmail(self):
        response = self.web_interface.manageEmail('testUser', 'testEmail')
        self.assertEqual(response, 'emailSuccess')

    def test_deployOnline(self):
        response = self.web_interface.deployOnline()
        self.assertTrue(response)

    def test_deployLocal(self):
        response = self.web_interface.deployLocal()
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()
```