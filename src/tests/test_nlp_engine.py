```python
import unittest
from src.nlp_engine import NlpEngine

class TestNlpEngine(unittest.TestCase):

    def setUp(self):
        self.nlp_engine = NlpEngine()

    def test_extract_information(self):
        query = "Schedule a meeting with John on Monday at 10 AM"
        expected_result = {
            'task': 'meeting',
            'with': 'John',
            'day': 'Monday',
            'time': '10 AM'
        }
        self.assertEqual(self.nlp_engine.extract_information(query), expected_result)

    def test_generate_response(self):
        query = "When is my next meeting?"
        expected_response = "Your next meeting is on Monday at 10 AM with John."
        self.assertEqual(self.nlp_engine.generate_response(query), expected_response)

    def test_understand_query(self):
        query = "Cancel my meeting with John on Monday"
        expected_result = {
            'action': 'cancel',
            'task': 'meeting',
            'with': 'John',
            'day': 'Monday'
        }
        self.assertEqual(self.nlp_engine.understand_query(query), expected_result)

if __name__ == '__main__':
    unittest.main()
```