```python
import unittest
from src.security import encryptData, decryptData

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.plain_text = "AI Scheduling Assistant"
        self.encrypted_text = encryptData(self.plain_text)

    def test_encryptData(self):
        self.assertNotEqual(self.plain_text, self.encrypted_text, "Encryption failed")

    def test_decryptData(self):
        decrypted_text = decryptData(self.encrypted_text)
        self.assertEqual(self.plain_text, decrypted_text, "Decryption failed")

if __name__ == '__main__':
    unittest.main()
```