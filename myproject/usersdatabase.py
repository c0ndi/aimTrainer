from myproject.__init__ import db

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
