from flask_app import app
from flask.ext.heroku import Heroku

heroku = Heroku(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
