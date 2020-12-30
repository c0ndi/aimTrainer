import os
from flask import Flask, render_template, redirect, url_for, session, flash
from myproject.forms import LoginForm, LogoutForm, GoToLoginForm
from flask_sqlalchemy import SQLAlchemy
from myproject.views import app, db
from usersdatabase import Users


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
