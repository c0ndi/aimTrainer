from myproject.__init__ import app
import os
from flask import Flask, render_template, redirect, url_for, session, flash
from myproject.forms import LoginForm, LogoutForm, GoToLoginForm
from flask_sqlalchemy import SQLAlchemy
from myproject.__init__ import app, db
from usersdatabase import Users


@app.route(f"/userpage/<login>")
def info(login):
    return 'Nick:' + session['nick']

@app.route('/rejestracja', methods = ['GET', 'POST'])
def rejestracja():

    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        nick = form.nick.data
        password = form.password.data

        if len(login) > 0 and len(nick) > 0 and len(password) > 0 and login != '' and nick != '' and password != '':
            user = Users(login, nick, password)
            users = (Users.query.filter_by(login = login, nick = nick)).all()
            nick = str(user).split(',')[1]
            login = (str(user).split(',')[0])[0:]
            session['login'] = login
            session['nick'] = nick
            if not nick and not login:
                return "<p>Niestety ale taki użytkownik już istnieje</p><a href=''/rejestracja'><button>Powrót</button></a>"
            else:
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


    return render_template('rejestracja.html', form = form, user = None)

@app.route('/logowanie', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    session['adminloggedin'] = False
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        if login != '' and password != '':
            if not (Users.query.filter_by(login = login, password = password)).all():
                #Nie ma takiego użytkownika
                flash('Niepoprawny login lub haslo')
            else:
                if login == 'Admin' and password == '1234':
                    session['adminloggedin'] = True
                else:
                    user = (Users.query.filter_by(login = login, password = password)).all()
                    session['nick'] = str(user).split(',')[1]
                return redirect(url_for('game'))

    return render_template('logowanie.html', form = form, user = None)


@app.route('/game', methods = ["POST", "GET"])
def game():
    logoutform = LogoutForm()
    loginform = GoToLoginForm()
    if len(session.keys()) < 2:
        return render_template('game-page.html', user = None, form = logoutform, loginform = loginform)
    if logoutform.validate_on_submit():
        session['nick'] = ''
        session['adminloggedin'] = False
        return redirect(url_for('game'))
    elif loginform.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('game-page.html', user = session['nick'], form = logoutform, loginform = loginform, login = session['nick'])


@app.route('/', methods = ["POST", "GET"])
def index():
    logoutform = LogoutForm()
    loginform = GoToLoginForm()
    if len(session.keys()) < 2:
        return render_template('main-page.html', user = None)
    if loginform.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('main-page.html', user = session['nick'], form = logoutform, loginform = loginform)

@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
  return render_template("404.html")
