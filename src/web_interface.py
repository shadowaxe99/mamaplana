```python
from flask import Flask, render_template, request, redirect, url_for
from src.user_account import loginUser, signupUser
from src.ai_scheduler import scheduleTask
from src.email_integration import manageEmail

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user_data = request.form
    login_success = loginUser(user_data)
    if login_success:
        return redirect(url_for('home'))
    else:
        return 'Login Failed', 401

@app.route('/signup', methods=['POST'])
def signup():
    user_data = request.form
    signup_success = signupUser(user_data)
    if signup_success:
        return redirect(url_for('home'))
    else:
        return 'Signup Failed', 400

@app.route('/schedule', methods=['POST'])
def schedule():
    schedule_data = request.form
    schedule_success = scheduleTask(schedule_data)
    if schedule_success:
        return 'Task Scheduled Successfully'
    else:
        return 'Scheduling Failed', 400

@app.route('/email', methods=['POST'])
def email():
    email_data = request.form
    email_success = manageEmail(email_data)
    if email_success:
        return 'Email Sent Successfully'
    else:
        return 'Email Failed', 400

if __name__ == '__main__':
    app.run(debug=True)
```