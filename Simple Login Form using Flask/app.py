from flask import Flask,render_template,request,redirect

app = Flask(__name__)

users = [
    {'username': 'admin', 'password': 'password123'},
    {'username': 'user', 'password': '123456'}
]


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            # Successful login, redirect to a dashboard or homepage
            return redirect('/dashboard')

    # Login failed, show an error message
    error_message = 'Invalid username or password.'
    return render_template('login.html', error_message=error_message)


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'



if __name__=="__main__":
    app.run(host="0.0.0.0")
