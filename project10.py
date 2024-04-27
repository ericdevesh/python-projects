#Write a python code to build web pages with sign-in and sing-up forms

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data (in real application, use a database)
users = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username is already taken
        if username in users:
            return "Username already taken. Please choose a different username."
        # Add the new user to the database
        users[username] = password
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username exists and password is correct
        if username in users and users[username] == password:
            return "Login successful! Welcome, " + username + "!"
        else:
            return "Invalid username or password. Please try again."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
