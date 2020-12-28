from flask import Flask, render_template, redirect, url_for
from loginform import LoginForm
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aimtrainer'

mysql = MySQL(app)

@app.route('/rejestracja', methods = ['GET', 'POST'])
def rejestracja():

    form = LoginForm()

    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        if login != '' and password != '':
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(login, password) VALUES (%s, %s)", (login, password))
            mysql.connection.commit()
            cur.close()

        return redirect(url_for('game'))

    return render_template('rejestracja.html', form = form)

@app.route('/logowanie', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        if login != '' and password != '':
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM users WHERE login = % s AND password = % s', (login, password, ))
            account = cur.fetchone()
            mysql.connection.commit()
            cur.close()
            if account:
                return redirect(url_for('game'))
            else:
                return 'Nie udało się zalogować'



    return render_template('logowanie.html', form = form)

@app.route('/game')
def game():
    return render_template('game-page.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
