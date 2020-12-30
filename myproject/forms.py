from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):

    login = StringField('Login')
    nick = StringField('Nick')
    password = PasswordField('Password')
    submit = SubmitField('Zaloguj')

class LogoutForm(FlaskForm):
    submit = SubmitField('Wyloguj')

class GoToLoginForm(FlaskForm):
    submit = SubmitField('Logowanie')
