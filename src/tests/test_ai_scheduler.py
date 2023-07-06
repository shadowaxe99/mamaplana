```python
import unittest
from src.ai_scheduler import AIScheduler

class TestAIScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = AIScheduler()
        self.userPreferences = {"timezone": "EST", "working_hours": "9-5"}
        self.userAccount = {"username": "test_user", "password": "test_password"}
        self.calendarData = {"events": []}
        self.emailData = {"inbox": []}

    def test_scheduleTask(self):
        task = {"title": "Meeting", "time": "10:00", "duration": "1h"}
        self.scheduler.scheduleTask(task, self.userPreferences, self.calendarData)
        self.assertIn(task, self.calendarData["events"])

    def test_manageEmail(self):
        email = {"subject": "Test", "body": "This is a test email."}
        self.scheduler.manageEmail(email, self.emailData)
        self.assertIn(email, self.emailData["inbox"])

    def test_loginUser(self):
        self.scheduler.loginUser(self.userAccount)
        self.assertTrue(self.scheduler.isLoggedIn)

    def test_signupUser(self):
        new_user = {"username": "new_user", "password": "new_password"}
        self.scheduler.signupUser(new_user)
        self.assertIn(new_user, self.scheduler.users)

if __name__ == '__main__':
    unittest.main()
```