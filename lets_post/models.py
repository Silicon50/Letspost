from  datetime import datetime
from itsdangerous import URLSafeTimedSerializer #for generating token to reset password
from lets_post import db, login_manager, app
from flask_login import UserMixin #is authenticated,active,anonymous,get_id attributes and methods

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader:
    This is a decorator provided by Flask-Login. It registers the load_user function with Flask-Login’s LoginManager.
    The user_loader decorator tells Flask-Login how to load a user from a user ID that is stored in the session.
    Flask-Login needs this function to retrieve a user object when a user is logged in.
    def load_user(user_id)::
    This function is responsible for retrieving the user object corresponding to the provided user ID.
    User.query.get is a method provided by SQLAlchemy, the ORM (Object-Relational Mapper) used by Flask-SQLAlchemy. It queries the database for a record with the primary key equal to user_id.
    '''
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    '''
        User information column showing
        user id as the primary key, username, email, password and image file for user image.
        the user image can be set to default.jpg if not uploaded.
        posts share a relationship with the Post class. backref allows the post to access the user using author
    '''
    id = db.Column(db.Integer, primary_key=True )
    username =db.Column(db.String(20), unique =True, nullable = False)
    email = db.Column(db.String(100), unique =True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg') 
    password = db.Column(db.String(20), nullable = False)
    posts = db.relationship('Post', backref = 'author', lazy = True)
    
    def get_reset_token(self, expires_sec = 1800):
        '''generate a token for password reset'''
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})
    
    @staticmethod
    def verify_reset_token(token, expires_sec = 1800):
        '''verify the token for password reset'''
        s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, expires_sec)['user_id']
        except:
            return None
        return User.query.get(user_id)
        
    def __repr__(self):
        '''representation of the user '''
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    
class Post(db.Model):
    '''
        The post class which accept the users post and save in the database
        Post id as the primary key, title, content. user_id as the foreign key that connects to the User_id
        the data_posted get the cureent date using the utcnow from datetime module
    '''
    id =  db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.DateTime, nullable =False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
