from myproject.views import app, db


if __name__ == '__main__':
    print()
    db.create_all()
    app.run(debug = True)
