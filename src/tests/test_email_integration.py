```python
import unittest
from src import email_integration

class TestEmailIntegration(unittest.TestCase):

    def setUp(self):
        self.emailData = {
            "email": "test@example.com",
            "subject": "Test Subject",
            "body": "Test Body"
        }
        self.emailIntegration = email_integration.EmailIntegration(self.emailData)

    def test_manageEmail(self):
        result = self.emailIntegration.manageEmail()
        self.assertEqual(result, "emailSuccess")

    def test_extractInformation(self):
        query = "Schedule a meeting with John on Monday at 10 AM"
        expected_result = {
            "contact": "John",
            "day": "Monday",
            "time": "10 AM"
        }
        result = self.emailIntegration.extractInformation(query)
        self.assertEqual(result, expected_result)

    def test_generateResponse(self):
        query = "When is my next meeting?"
        expected_result = "Your next meeting is on Monday at 10 AM with John."
        result = self.emailIntegration.generateResponse(query)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
```