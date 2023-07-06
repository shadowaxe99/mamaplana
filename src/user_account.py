```python
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from src.security import encryptData, decryptData
from src import db

class UserSchema(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    preferences = db.Column(db.String(500))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_preferences(self, preferences):
        self.preferences = encryptData(preferences)

    def get_preferences(self):
        return decryptData(self.preferences)

def loginUser(username, password):
    user = UserSchema.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return {'status': 'success', 'message': 'loginSuccess', 'user': user}
    else:
        return {'status': 'error', 'message': 'Invalid username or password'}

def signupUser(username, email, password):
    user = UserSchema(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {'status': 'success', 'message': 'signupSuccess', 'user': user}
```