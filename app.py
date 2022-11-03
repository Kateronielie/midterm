from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
# app.secret_key = "__privatekey__"


#FOR INDEX PAGE REDIRECT
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
if __name__ == "__main__":
    app.run(debug=True)


