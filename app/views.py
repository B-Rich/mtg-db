from flask import render_template, redirect, url_for
from app import app
# from .util import ts, send_email
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Jace Beleren'} # placeholder user
    return render_template('index.html',
                           title='home',
                           user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template("login.html",
                           title = "Sign In",
                           form = form)
