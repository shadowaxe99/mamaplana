```python
from cryptography.fernet import Fernet

class Security:

    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encryptData(self, data):
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decryptData(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

    def secureUserAccount(self, userAccount):
        encryptedAccount = self.encryptData(userAccount)
        return encryptedAccount

    def retrieveUserAccount(self, encryptedAccount):
        decryptedAccount = self.decryptData(encryptedAccount)
        return decryptedAccount

    def secureCalendarData(self, calendarData):
        encryptedData = self.encryptData(calendarData)
        return encryptedData

    def retrieveCalendarData(self, encryptedData):
        decryptedData = self.decryptData(encryptedData)
        return decryptedData

    def secureEmailData(self, emailData):
        encryptedData = self.encryptData(emailData)
        return encryptedData

    def retrieveEmailData(self, encryptedData):
        decryptedData = self.decryptData(encryptedData)
        return decryptedData
```