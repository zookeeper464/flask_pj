from .app import db

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)

    u_matchs = db.relationship('Match', backref='author', lazy=True)

    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

class Match(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'), nullable=False)

    def __repr__(self):
        return f"User ('{self.user_id}','{self.music_id}')"

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    musician = db.Column(db.String(100), nullable=False)
    tag1 = db.Column(db.String(50), nullable=False)
    tag2 = db.Column(db.String(50), nullable=True)
    tag3 = db.Column(db.String(50), nullable=True)
    
    m_match = db.relationship('Match', backref='author', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.musician}')"    