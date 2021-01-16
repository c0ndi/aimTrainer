import os
from flask import Flask, render_template, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from myproject.forms import LoginForm, LogoutForm
from myproject.__init__ import app, db
from myproject.usersdatabase import Users



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

            if user.exist():
                flash('Niestety ale taki użytkownik istnieje')

            else:
                session['login'] = login
                session['nick'] = nick
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


    return render_template('rejestracja.html', form = form, user = None)

@app.route('/logowanie', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        if login != '' and password != '':
            users = (Users.query.filter_by(login = login, password = password)).all()
            if not users:
                #Nie ma takiego użytkownika
                flash('Niepoprawny login lub haslo')
            else:
                session['nick'] = str(users).split(',')[1]
                return redirect(url_for('game'))

    return render_template('logowanie.html', form = form, user = None)


@app.route('/game', methods = ["POST", "GET"])
def game():
    logoutform = LogoutForm()
    if 'nick' not in session:
        return render_template('game-page.html', user = None, form = logoutform)
    if logoutform.validate_on_submit():
        session['nick'] = ''
        session['adminloggedin'] = False
        print(session.get('score'))
        return redirect(url_for('game'))

    return render_template('game-page.html', user = session['nick'], form = logoutform, login = session['nick'])


@app.route('/', methods = ["POST", "GET"])
def index():
    if len(session.keys()) < 2:
        return render_template('main-page.html', user = None)
    return render_template('main-page.html', user = session['nick'])

@app.errorhandler(404)
def not_found(e):

  return render_template("404.html")
