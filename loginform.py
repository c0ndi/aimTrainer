from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):

    login = StringField('Login')
    password = PasswordField('Password')
    submit = SubmitField('Zaloguj')
