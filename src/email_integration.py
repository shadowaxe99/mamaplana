```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailIntegration:
    def __init__(self, emailData):
        self.emailData = emailData

    def connect_to_server(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.emailData['email'], self.emailData['password'])
            return server
        except Exception as e:
            print(f"Error: {e}")
            return None

    def send_email(self, to_email, subject, message):
        server = self.connect_to_server()
        if server:
            msg = MIMEMultipart()
            msg['From'] = self.emailData['email']
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            text = msg.as_string()
            server.sendmail(self.emailData['email'], to_email, text)
            server.quit()

    def manageEmail(self, emailForm):
        to_email = emailForm['to_email']
        subject = emailForm['subject']
        message = emailForm['message']
        self.send_email(to_email, subject, message)
        return 'emailSuccess'
```