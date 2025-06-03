from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="127.0.0.1")