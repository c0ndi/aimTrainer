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

    def exist(self):
        users = (Users.query.filter_by(login = self.login, nick = self.nick)).all()

        if not self.login and not self.nick:
            return True
        else:
            return False

    def valid(login, password):
        users = (Users.query.filter_by(login = login, password = password)).all()
        if not login and not password:
            return True
        else:
            return False
