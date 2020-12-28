import os
from flask import Flask, render_template, redirect, url_for, session
from loginform import LoginForm
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.Text)
    nick = db.Column(db.Text)
    password = db.Column(db.Text)
    max_score = db.Column(db.Integer)

    def __init__(self, login, nick, password):
        self.login = login
        self.nick = nick
        self.password = password

    def __repr__(self):
        return self.login + ',' + self.nick+ ',' +self.password

db.create_all()

@app.route('/rejestracja', methods = ['GET', 'POST'])
def rejestracja():

    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        nick = form.nick.data
        password = form.password.data

        if login != '' and password != '':
            user = Users(login, nick, password)
            db.session.add(user)
            db.session.commit()

        return redirect(url_for('game'))

    return render_template('rejestracja.html', form = form, user = None)

@app.route('/logowanie', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data
        if login != '' and password != '':
            if not (Users.query.filter_by(login = login, password = password)).all():
                #Nie ma takiego użytkownika
                return '<p>Niestety nie udało się zalogować</p>'
            else:
                #Jest taki użytkownik
                user = (Users.query.filter_by(login = login, password = password)).all()
                session['nick'] = str(user).split(',')[1]
                return redirect(url_for('game'))

    return render_template('logowanie.html', form = form, user = None)

@app.route('/game')
def game():
    if len(session.keys()) < 2:
        return render_template('game-page.html', user = None)
    return render_template('game-page.html', user = session['nick'])


@app.route('/')

def index():
    if len(session.keys()) < 2:
        return render_template('index.html', user = None)
    return render_template('index.html', user = session['nick'])

if __name__ == '__main__':
    app.run(debug = True)
