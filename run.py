from flask_app import app, db

if __name__ == '__main__':
    # app.debug = True
    db.create_all()
    db.configure_mappers()
    app.run()
