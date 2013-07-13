from app import Base
import hashlib, uuid

class User(Base):
    """System user record"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128), nullable = False)
    salt = db.Column(db.String(36), nullable = False)

    def _encrypt_password(password):
        """hashes the given password with a random salt, returns both"""
        salt = uuid.uuid4().hex
        return {salt: salt, hashed: hashlib.sha512(password + salt).hexdigest()}

    def __init__(self, email, password):
        self.username = username
        self.email = email
        password_data = self._encrypt_password(password)
        self.password = password_data['hashed']
        self.salt = password_data['salt']

    def __repr__(self):
        return '<User %r>' % self.email