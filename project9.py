#Write a python code to build web page with student registration form

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registration_form.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    roll_number = request.form['roll_number']
    age = request.form['age']
    grade = request.form['grade']
    # Process the registration data here
    return "Registration Successful"

if __name__ == '__main__':
    app.run(debug=True)
