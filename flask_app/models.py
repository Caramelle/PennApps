from flask_app import db

class Gifs(db.Model):
    __tablename__ = 'gifs'
    id = db.Column(db.Integer, primary_key=True)

    url = db.Column(db.String)
    number = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users', back_populates='gifs')

    def __repr__(self):
        return self.url

    def __init__(self, url, number, user):
        self.url = url
        self.number = number
        self.user = user

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    gifs = db.relationship('Gifs', back_populates='user', cascade='all, delete-orphan')
    
    current_slide = db.Column(db.Integer)
    current_max = db.Column(db.Integer)

    presentation_url = db.Column(db.String)

    def __init__(self):
        self.current_slide = 0
        
def add_user():
    new = Users()
    db.session.add(new)
    db.session.commit()
    return new.id

def get_user(id):
    u = Users.query.get(id)
    if not u:
        return False
    return u

def add_gif(url, slide, user):
    new = Gifs(url, slide, user)
    db.session.add(new)
    db.session.commit()
    return

def get_gif(id):
    g = Gifs.query.get(id)
    if not g:
        return False
    return g

def get_gifs(user):
    slide = user.current_slide
    gifs = Gifs.query.filter(Gifs.number==slide, Gifs.user == user).all()
    user.current_slide += 1
    db.session.commit()
    return gifs

def clear_db(user):
    u = get_user(user)
    Gifs.query.filter(Gifs.user == u).delete()
    db.session.delete(u)
    db.session.commit()
    return
