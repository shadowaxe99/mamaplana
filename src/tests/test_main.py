import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.userPreferences = main.userPreferences
        self.userAccount = main.userAccount
        self.calendarData = main.calendarData
        self.emailData = main.emailData

    def test_loginUser(self):
        result = main.loginUser(self.userAccount)
        self.assertEqual(result, "loginSuccess")

    def test_signupUser(self):
        result = main.signupUser(self.userAccount)
        self.assertEqual(result, "signupSuccess")

    def test_scheduleTask(self):
        result = main.scheduleTask(self.userPreferences, self.calendarData)
        self.assertEqual(result, "scheduleSuccess")

    def test_manageEmail(self):
        result = main.manageEmail(self.emailData)
        self.assertEqual(result, "emailSuccess")

    def test_deployOnline(self):
        result = main.deployOnline()
        self.assertTrue(result)

    def test_deployLocal(self):
        result = main.deployLocal()
        self.assertTrue(result)

    def test_encryptData(self):
        encrypted_data = main.encryptData(self.userAccount)
        decrypted_data = main.decryptData(encrypted_data)
        self.assertEqual(decrypted_data, self.userAccount)

    def test_releaseVersion(self):
        result = main.releaseVersion()
        self.assertTrue(result)

    def test_deployVersion(self):
        result = main.deployVersion()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()