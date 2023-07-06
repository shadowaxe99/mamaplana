import unittest
from src import agile_methods

class TestAgileMethods(unittest.TestCase):

    def setUp(self):
        self.agile_methods = agile_methods.AgileMethods()

    def test_iterative_development(self):
        result = self.agile_methods.iterative_development()
        self.assertTrue(result)

    def test_regular_feedback(self):
        feedback = "This is a feedback"
        result = self.agile_methods.regular_feedback(feedback)
        self.assertEqual(result, feedback)

    def test_continuous_improvement(self):
        initial_version = 1.0
        improved_version = self.agile_methods.continuous_improvement(initial_version)
        self.assertGreater(improved_version, initial_version)

if __name__ == '__main__':
    unittest.main()